from threading import Thread
import log


class MusicEngine:
    def __init__(self):
        self.is_playing = False
        self.formats = ("mp3",)
        self.logger = log.logger
        self.current_file = None
        self.music_thread = Thread()
        self.logger.debug("Music engine started")

    def play(self):
        self.is_playing = True
        print("Music is playing!!!")
        pass

    def pause(self):
        self.is_playing = False
        print("Music paused")
        pass

    def stop(self):
        self.is_playing = False
        print("Music paused")
        pass
