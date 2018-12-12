from windows import MainWindow


class App:

    def run(self):
        MainWindow().mainloop()

if __name__ == "__main__":
    instance = App()
    instance.run()
