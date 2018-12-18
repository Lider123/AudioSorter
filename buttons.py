from music import MusicEngine
from tkinter import Button, filedialog
import log


class PlayPauseButton(Button):

    def __init__(self, name, master):
        super(PlayPauseButton, self).__init__(master,
                                              text="play",
                                              width=10, height=5,
                                              bg="black", fg="white",
                                              command=self.onclick)
        self.logger = log.logger
        self.name = name

    def onclick(self):
        self.logger.debug("Button %s was presses" % self.name)
        if self["text"] == "play":
            MusicEngine.play()
            self["text"] = "pause"
        elif self["text"] == "pause":
            MusicEngine.pause()
            self["text"] = "play"


class BrowseDirButton(Button):
    def __init__(self, name, master):
        super(BrowseDirButton, self).__init__(master, text="browse:", command=self.onclick)
        self.logger = log.logger
        self.path = None
        self.name = name

    def onclick(self):
        self.logger.debug("Button %s was presses" % self.name)
        self.path = filedialog.askopenfilename(initialdir="~", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.logger.debug("Choosed directory: %s" % self.path)


class LikeButton(Button):
    def __init__(self, name, master):
        super(LikeButton, self).__init__(master, text="like", command=self.onclick)
        self.logger = log.logger
        self.name = name

    def onclick(self):
        self.logger.debug("Button %s was presses" % self.name)
        pass


class DislikeButton(Button):
    def __init__(self, name, master):
        super(DislikeButton, self).__init__(master, text="dislike", command=self.onclick)
        self.logger = log.logger
        self.name = name

    def onclick(self):
        self.logger.debug("Button %s was presses" % self.name)
        pass
