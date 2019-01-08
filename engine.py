from send2trash import send2trash
import errno
import log
import os
import random
import re
import shutil


class FileEngine:
    def __init__(self):
        self.logger = log.logger
        self.source_files = list()
        self.logger.debug("File engine has been started")

    def find_source_files(self, path, formats):
        """Find all files of specified formats in the specified directory and subdirectories"""
        self.source_files = list()
        for root, directories, filenames in os.walk(path):
            for filename in filenames:
                if any([re.search(r".{f}$".format(f=f), filename) for f in formats]):
                    self.source_files.append(os.path.relpath(os.path.join(root, filename), path))
        random.shuffle(self.source_files)
        self.logger.debug("Found %d files in directory %s and it's subdirectories" % (self.get_files_count(), path))
        return

    def move_current_file(self, src, dest):
        """Move current file to specified directory"""
        curr_file = self.get_current_file()
        fullsrc = os.path.join(src, curr_file)
        fulldest = os.path.join(dest, curr_file)
        if not os.path.exists(os.path.dirname(fulldest)):
            try:
                os.makedirs(os.path.dirname(fulldest))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        shutil.move(fullsrc, fulldest)

        self.logger.debug("File %s has been moved to directory %s" % (curr_file, dest))
        self.source_files.pop(0)
        return

    def delete_current_file(self, src):
        curr_file = self.get_current_file()
        fullpath = os.path.join(src, curr_file)
        fulltrash = os.path.join("C:\\Users\\User\\AudioSorterTrash", curr_file)
        if not os.path.exists(os.path.dirname(fulltrash)):
            try:
                os.makedirs(os.path.dirname(fulltrash))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        shutil.move(fullpath, fulltrash)

        self.logger.debug("File %s has been deleted" % curr_file)
        self.source_files.pop(0)
        return

    def get_current_file(self):
        return self.source_files[0]

    def get_files_count(self):
        return len(self.source_files)
