from buttons import *
import tkinter as tk


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setup()

    def setup(self):
        self.title("AudioSorter")
        self.geometry("600x600")
        self.resizable(0, 0)

        ppbutton = PlayPauseButton("PlayPauseButton", self)
        ppbutton.place(relx=0.5, rely=0.5, anchor="center")

        bdbutton1 = BrowseDirButton("ChooseSourceButton", self)
        bdbutton1.place(relx=0.0, rely=1.0, anchor="sw")
        browse_downloads_label = tk.Label(text="Downloads dir")
        browse_downloads_label.place(relx=0.0, rely=0.95, anchor="sw")

        bdbutton2 = BrowseDirButton("ChooseDestinationButton", self)
        bdbutton2.place(relx=1.0, rely=1.0, anchor="se")
        browse_liked_label = tk.Label(text="Liked dir")
        browse_liked_label.place(relx=1.0, rely=0.95, anchor="se")

        lbutton = LikeButton("LikeButton", self)
        lbutton.place(relx=0.4, rely=1.0, anchor="s")

        dbutton = DislikeButton("DislikeButton", self)
        dbutton.place(relx=0.6, rely=1.0, anchor="s")

        return
