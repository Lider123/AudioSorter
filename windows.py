from buttons import PlayPauseButton
import tkinter as tk


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setup()

    def setup(self):
        self.title("AudioSorter")
        self.geometry("600x600")
        self.resizable(0, 0)

        label = tk.Label(self, text="There will be audio player!")
        label.pack()

        b = PlayPauseButton(self)
        b.pack()

        return
