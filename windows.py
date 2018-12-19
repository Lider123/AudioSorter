from music import MusicEngine
from tkinter import Label, Button, filedialog, Tk
import log
import tkinter as tk


class MainWindow(Tk):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.WIDTH = 600
        self.HEIGHT = 600
        self.source_dir = ""
        self.dest_dir = ""
        self.logger = log.logger
        self.setup()

    def setup(self):
        self.title("AudioSorter")
        self.geometry("%dx%d" % (self.WIDTH, self.HEIGHT))
        self.resizable(0, 0)

        self.playpauseButton = Button(self, text="play", width=10, height=5, bg="black", fg="white", command=self.onPlayPauseButtonClick)
        self.playpauseButton.place(relx=0.5, rely=0.5, anchor="center")

        self.choosesourcedirButton = Button(self, text="browse:", command=self.onChooseSourceDirButtonClick)
        self.choosesourcedirButton.place(relx=0.0, rely=1.0, anchor="sw")
        self.browse_downloads_label = Label(text="Downloads dir")
        self.browse_downloads_label.place(relx=0.0, rely=0.95, anchor="sw")

        self.choosedestdirButton = Button(self, text="browse:", command=self.onChooseDestDirButtonClick)
        self.choosedestdirButton.place(relx=1.0, rely=1.0, anchor="se")
        self.browse_liked_label = Label(text="Liked dir")
        self.browse_liked_label.place(relx=1.0, rely=0.95, anchor="se")

        self.likebutton = Button(self, text="like", command=self.onLikeButtonClick)
        self.likebutton.place(relx=0.4, rely=1.0, anchor="s")

        self.dislikebutton = Button(self, text="dislike", command=self.onDislikeButtonClick)
        self.dislikebutton.place(relx=0.6, rely=1.0, anchor="s")

        return

    def onPlayPauseButtonClick(self):
        self.logger.debug("PlayPauseButton was pressed")
        if not MusicEngine.is_playing:
            MusicEngine.play()
            MusicEngine.is_playing = True
            self.playpauseButton["text"] = "pause"
        else:
            MusicEngine.pause()
            MusicEngine.is_playing = False
            self.playpauseButton["text"] = "play"
        return

    def onChooseSourceDirButtonClick(self):
        self.logger.debug("Button ChooseSourceDir was presses")
        new_path = filedialog.askdirectory(initialdir="~", title="Select directory", mustexist=True)
        if len(new_path) > 0:
            self.source_dir = new_path
            self.logger.debug("Choosed directory: %s" % self.source_dir)
        else:
            self.logger.debug("Directory was not been chosen")

    def onChooseDestDirButtonClick(self):
        self.logger.debug("Button ChooseDestDir was presses")
        new_path = filedialog.askdirectory(initialdir="~", title="Select directory", mustexist=True)
        if len(new_path) > 0:
            self.dest_dir = new_path
            self.logger.debug("Choosed directory: %s" % self.dest_dir)
        else:
            self.logger.debug("Directory was not been chosen")

    def onLikeButtonClick(self):
        self.logger.debug("Button LikeButton was presses")
        pass

    def onDislikeButtonClick(self):
        self.logger.debug("Button DislikeButton was presses")
        pass