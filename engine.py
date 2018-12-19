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
        self.source_files = list()
        for root, directories, filenames in os.walk(path):
            for filename in filenames:
                if any([re.search(r".{f}$".format(f=f), filename) for f in formats]):
                    self.source_files.append(os.path.relpath(os.path.join(root, filename), path))
        random.shuffle(self.source_files)
        self.logger.debug("Found %d files" % len(self.source_files))
        return

    def move_current_file(self, path):
        pass

    def delete_current_file(self):
        pass

    def get_current_file(self):
        return self.source_files[0]

    def get_files_count(self):
        return len(self.source_files)
