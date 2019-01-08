from buttons import DislikeButton, PlayPauseButton, LikeButton
from engine import FileEngine
from music import MusicEngine
from tkinter import Label, Button, filedialog, messagebox, Tk
import log
import os


class MainWindow(Tk):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.WIDTH = 800
        self.HEIGHT = 600
        self.source_dir = ""
        self.dest_dir = ""

        self.logger = log.logger

        self.playpause_button = None
        self.choosesourcedir_button = None
        self.choosedestdir_button = None
        self.like_button = None
        self.dislike_button = None

        self.filename_label = None
        self.browse_downloads_label = None
        self.browse_liked_label = None

        self.setup()

        self.file_engine = FileEngine()
        self.music_engine = MusicEngine(self.playpause_button)

    def setup(self):
        self.title("AudioSorter")
        self.geometry("%dx%d" % (self.WIDTH, self.HEIGHT))
        self.resizable(0, 0)
        self["bg"] = "#F7931A"

        self.filename_label = Label(text="file", bg=self["bg"])
        self.filename_label.place(relx=0.5, rely=0.1, anchor="n")

        self.playpause_button = PlayPauseButton(self, bg=self["bg"], command=self.on_playpause_button_click)
        self.playpause_button.place(relx=0.5, rely=0.5, anchor="center")

        self.choosesourcedir_button = Button(self, text="browse", height=3, command=self.on_choosesourcedir_button_click)
        self.choosesourcedir_button.place(relx=0.0, rely=1.0, anchor="sw")
        self.browse_downloads_label = Label(text="Downloads dir:", bg=self["bg"])
        self.browse_downloads_label.place(relx=0.0, rely=0.90, anchor="sw")

        self.choosedestdir_button = Button(self, text="browse", height=3, command=self.on_choosedestdir_button_click)
        self.choosedestdir_button.place(relx=1.0, rely=1.0, anchor="se")
        self.browse_liked_label = Label(text="Liked dir:", bg=self["bg"])
        self.browse_liked_label.place(relx=1.0, rely=0.90, anchor="se")

        self.like_button = LikeButton(self, bg=self["bg"], command=self.on_like_button_click)
        self.like_button.place(relx=0.4, rely=1.0, anchor="s")

        self.dislike_button = DislikeButton(self, bg=self["bg"], command=self.on_dislike_button_click)
        self.dislike_button.place(relx=0.6, rely=1.0, anchor="s")

        self.logger.debug("The main window has been configured")
        return

    def on_playpause_button_click(self):
        self.logger.debug("PlayPauseButton has been pressed")

        """If no source and destination directories are selected"""
        if not self.source_dir:
            self.logger.debug("No chosen source directory. Redirecting to dialog window")
            self.on_choosesourcedir_button_click()
        if not self.dest_dir:
            self.logger.debug("No chosen destination directory. Redirecting to dialog window")
            self.on_choosedestdir_button_click()
        if not (self.source_dir and self.dest_dir):
            return

        """If there are no files in source directory"""
        if not self.check_files_count():
            self.logger.debug("There are no files in directory %s" % self.source_dir)
            return

        if not self.music_engine.is_playing:
            self.music_engine.play()
            self.filename_label["text"] = self.file_engine.get_current_file()
        else:
            self.music_engine.pause()
        return

    def on_choosesourcedir_button_click(self):
        self.logger.debug("Button ChooseSourceDir has been pressed")
        self.stop_playing()

        new_path = filedialog.askdirectory(initialdir="~", title="Select source directory", mustexist=True)
        if not new_path:
            self.logger.debug("Source directory has not been chosen")
            return
        else:
            self.browse_downloads_label["text"] = "Downloads dir: " + new_path

        self.source_dir = new_path
        self.logger.debug("Chosen source directory: %s" % self.source_dir)

        self.file_engine.find_source_files(self.source_dir, self.music_engine.formats)
        if self.check_files_count():
            self.music_engine.set_file(self.fullpath(self.file_engine.get_current_file()))
        return

    def on_choosedestdir_button_click(self):
        self.logger.debug("Button ChooseDestDir has been pressed")
        new_path = filedialog.askdirectory(initialdir="~", title="Select destination directory", mustexist=True)
        if not new_path:
            self.logger.debug("Destination directory has not been chosen")
            return
        else:
            self.browse_liked_label["text"] = "Liked dir: " + new_path

        self.dest_dir = new_path
        self.logger.debug("Chosen destination directory: %s" % self.dest_dir)
        return

    def on_like_button_click(self):
        self.logger.debug("Button LikeButton has been pressed")

        if not self.check_files_count():
            return

        self.stop_playing()
        self.music_engine.clear_mixer()
        self.file_engine.move_current_file(self.source_dir, self.dest_dir)

        if not self.file_engine.get_files_count():
            self.music_engine.set_file(None)
        else:
            self.play_next()
        return

    def on_dislike_button_click(self):
        self.logger.debug("Button DislikeButton has been pressed")

        if not self.check_files_count():
            return

        self.stop_playing()
        self.music_engine.clear_mixer()
        self.file_engine.delete_current_file(self.source_dir)

        if not self.file_engine.get_files_count():
            self.music_engine.set_file(None)
        else:
            self.play_next()
        return

    def play_next(self):
        curr_file = self.file_engine.get_current_file()
        self.music_engine.set_file(self.fullpath(curr_file))
        self.music_engine.play()
        self.filename_label["text"] = curr_file
        return

    def stop_playing(self):
        if self.music_engine.is_playing:
            self.music_engine.stop()
        return

    def check_files_count(self):
        if not self.file_engine.get_files_count():
            messagebox.showinfo("Info", "There are no files in the source directory")
            self.filename_label["text"] = "file"
            return False
        return True

    def fullpath(self, path):
        return os.path.join(self.source_dir, path)
