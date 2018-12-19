import log
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
                    self.source_files.append(os.path.join(root, filename))
        self.logger.debug("Found %d files" % len(self.source_files))
