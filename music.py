from threading import Thread
import log


class MusicEngine:
    def __init__(self):
        self.is_playing = False
        self.formats = ("mp3", )
        self.logger = log.logger
        self.music_thread = Thread()
        self.logger.debug("Music engine started")

    def play(self):
        self.is_playing = True
        print("Music is playing!!!")

    def pause(self):
        self.is_playing = False
        print("Music stopped")
