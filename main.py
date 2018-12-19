from windows import MainWindow
import log


class App:
    def __init__(self):
        self.logger = log.logger
        self.logger.debug('Logger started')

    def run(self):
        main_window = MainWindow()
        self.logger.debug("App started")
        main_window.mainloop()

if __name__ == "__main__":
    instance = App()
    instance.run()
