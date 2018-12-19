from tkinter import Button, filedialog
import log


class DislikeButton(Button):
    def __init__(self, name, master):
        super(DislikeButton, self).__init__(master, text="dislike", command=self.onclick)
        self.logger = log.logger
        self.name = name

    def onclick(self):
        self.logger.debug("Button %s was presses" % self.name)
        pass
