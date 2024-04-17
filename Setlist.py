from Song import Song

class Setlist:
    songs: [Song]

    def __init__(self):
        self.songs = []

    def show(self):
        print("\nSetlist:\n")
        for song in sorted(self.songs, key=lambda x: x.votes, reverse=True):
            print(song)

    def order(self):
        pass

    def add(self, Song):
        self.songs.append(Song)

    def remove(self, name, artist):
        for song in self.songs:
            if song.name == name and song.artist == artist:
                self.songs.remove(song)