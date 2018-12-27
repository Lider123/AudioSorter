from tkinter import Button, PhotoImage


class PlayPauseButton(Button):
    def __init__(self, *args, **kwargs):
        super(PlayPauseButton, self).__init__(*args, **kwargs)
        self["image"] = self.play_img
        self["border"] = 0
        self.play_img = PhotoImage(file="assets/play.png")
        self.pause_img = PhotoImage(file="assets/pause.png")

    def set_play_img(self):
        self["image"] = self.play_img
        return

    def set_pause_img(self):
        self["image"] = self.pause_img
        return
