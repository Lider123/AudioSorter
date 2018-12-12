from music import MusicEngine
from tkinter import Button


class PlayPauseButton(Button):

    def __init__(self, master):
        super(PlayPauseButton, self).__init__(master,
                                              text="play",
                                              width=10, height=5,
                                              bg="black", fg="white",
                                              command=self.onclick)

    def onclick(self):
        if self["text"] == "play":
            MusicEngine.play()
            self["text"] = "pause"
        elif self["text"] == "pause":
            MusicEngine.pause()
            self["text"] = "play"


class BrowseDirButton(Button):

    def __init__(self, master):
        super(BrowseDirButton, self).__init__(master, text="browse:", command=self.onclick)

    def onclick(self):
        pass
