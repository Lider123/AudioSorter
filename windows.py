from engine import FileEngine
from music import MusicEngine
from tkinter import Label, Button, filedialog, Tk
import log


class MainWindow(Tk):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.WIDTH = 600
        self.HEIGHT = 600
        self.source_dir = ""
        self.dest_dir = ""

        self.logger = log.logger
        self.file_engine = FileEngine()
        self.music_engine = MusicEngine()

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
        if not self.source_dir:
            self.logger.debug("No chosen source directory. Redirecting to dialog window")
            self.onChooseSourceDirButtonClick()
        if not self.dest_dir:
            self.logger.debug("No chosen destination directory. Redirecting to dialog window")
            self.onChooseDestDirButtonClick()
        if not (self.source_dir and self.dest_dir):
            return

        if self.file_engine.get_files_count() == 0:
            print("There is no files")
            return

        if not self.music_engine.is_playing:
            self.music_engine.play()
            self.playpauseButton["text"] = "pause"
        else:
            self.music_engine.pause()
            self.playpauseButton["text"] = "play"
        return

    def onChooseSourceDirButtonClick(self):
        self.logger.debug("Button ChooseSourceDir was presses")
        new_path = filedialog.askdirectory(initialdir="~", title="Select source directory", mustexist=True)
        if not new_path:
            self.logger.debug("Source directory was not been chosen")
            return

        self.source_dir = new_path
        self.logger.debug("Choosed source directory: %s" % self.source_dir)

        self.file_engine.find_source_files(self.source_dir, self.music_engine.formats)
        if self.file_engine.get_files_count() == 0:
            print("There is no files")
        else:
            self.music_engine.current_file = self.file_engine.get_current_file()
        return

    def onChooseDestDirButtonClick(self):
        self.logger.debug("Button ChooseDestDir was presses")
        new_path = filedialog.askdirectory(initialdir="~", title="Select destination directory", mustexist=True)
        if not new_path:
            self.logger.debug("Destination directory was not been chosen")
            return

        self.dest_dir = new_path
        self.logger.debug("Choosed destination directory: %s" % self.dest_dir)
        return

    def onLikeButtonClick(self):
        self.logger.debug("Button LikeButton was presses")
        if self.music_engine.is_playing:
            self.music_engine.stop()
        self.file_engine.move_current_file(self.dest_dir)

        if self.file_engine.get_files_count() == 0:
            print("There is no files")
            return

        self.music_engine.current_file = self.file_engine.get_current_file()
        self.music_engine.play()
        self.playpauseButton["text"] = "pause"
        pass

    def onDislikeButtonClick(self):
        self.logger.debug("Button DislikeButton was presses")
        if self.music_engine.is_playing:
            self.music_engine.stop()
        self.file_engine.delete_current_file()

        if self.file_engine.get_files_count() == 0:
            print("There is no files")
            return

        self.music_engine.current_file = self.file_engine.get_current_file()
        self.music_engine.play()
        self.playpauseButton["text"] = "pause"
        pass
