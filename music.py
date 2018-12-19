class MusicEngine:
    is_playing = False
    formats = ("mp3", )

    @staticmethod
    def play():
        print("Music is playing!!!")

    @staticmethod
    def pause():
        print("Music stopped")
