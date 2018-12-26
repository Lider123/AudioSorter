import log
import random
import re
import os


class FileEngine:
    def __init__(self):
        self.logger = log.logger
        self.source_files = list()
        self.logger.debug("File engine started")

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

    def move_current_file(self, path):
        """Move current file to specified directory"""
        print("Moving file to the destination directory")
        self.logger.debug("File %s was moved to directory %s" % (self.get_current_file(), path))
        self.source_files.pop(0)
        pass

    def delete_current_file(self):
        print("Deleting file")
        self.logger.debug("File %s was deleted" % self.get_current_file())
        self.source_files.pop(0)
        pass

    def get_current_file(self):
        return self.source_files[0]

    def get_files_count(self):
        return len(self.source_files)
