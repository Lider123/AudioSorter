from music import MusicEngine
from tkinter import Button


class PlayPauseButton(Button):

    def __init__(self, window):
        super(PlayPauseButton, self).__init__(window, text="play", command=self.handle)

    def handle(self):
        if self["text"] == "play":
            MusicEngine.play()
            self["text"] = "pause"
        elif self["text"] == "pause":
            MusicEngine.pause()
            self["text"] = "play"
