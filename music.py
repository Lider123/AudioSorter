import log
import pygame


class MusicEngine:
    def __init__(self, master):
        self.is_playing = False
        self.paused = False
        self.formats = ("mp3",)
        self.logger = log.logger
        self.current_file = None
        self.master_button = master
        pygame.init()
        self.logger.debug("Music engine has been started")

    def set_file(self, path):
        self.current_file = open(path, 'rb')
        if path is not None:
            pygame.mixer.music.load(self.current_file)
        self.is_playing = False
        self.paused = False
        self.master_button.set_play_img()
        self.logger.debug("Ready to play file %s" % self.current_file.name)
        return

    def clear_mixer(self):
        filename = self.current_file.name
        self.current_file.close()
        self.logger.debug("File %s has been closed" % filename)
        return

    def play(self):
        self.is_playing = True
        if self.paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play(-1)
            self.logger.debug("Playing file %s" % self.current_file.name)
        self.master_button.set_pause_img()
        return

    def pause(self):
        self.is_playing = False
        self.paused = True
        pygame.mixer.music.pause()
        self.master_button.set_play_img()
        self.logger.debug("Music paused")
        return

    def stop(self):
        self.is_playing = False
        self.paused = False
        pygame.mixer.music.stop()
        self.master_button.set_play_img()
        self.logger.debug("Music stopped")
        return
