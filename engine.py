from music import MusicEngine
import log
import re
import os


class Engine:
    def __init__(self):
        self.source_files = list()
        self.logger = log.logger

    def find_source_files(self, path):
        self.source_files = list()
        for root, directories, filenames in os.walk(path):
            for filename in filenames:
                if any([re.search(r".{f}$".format(f=f), filename) for f in MusicEngine.formats]):
                    self.source_files.append(os.path.join(root, filename))
        self.logger.debug("Found %d files" % len(self.source_files))
        pass
