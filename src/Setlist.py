from src.Song import Song

class Setlist:
    songs: [Song]

    def __init__(self):
        self.songs = []

    def show(self):
        print("\nSetlist:\n")
        for song in sorted(self.songs, key=lambda x: x.votes, reverse=True):
            print(f"{song}\n")
        print(f"{len(self.songs)} total songs.")

    def findByName(self, name):
        counter = 0
        for song in self.songs:
            if name in song.name:
                print(f"{song}\n")
                counter += 1
        print(f"{counter} songs found.")

    def findByArtist(self, artist):
        counter = 0
        for song in self.songs:
            if artist in song.artist:
                print(f"{song}\n")
                counter += 1
        print(f"{counter} songs found.")

    def findByVotes(self, votes):
        counter = 0
        for song in self.songs:
            if song.votes == votes:
                print(f"{song}\n")
                counter += 1
        print(f"{counter} songs found.")

    def add(self, Song):
        self.songs.append(Song)

    def remove(self, name, artist):
        removed = False
        for song in self.songs:
            if song.name == name and song.artist == artist:
                print(f"Removing {song.name}...")
                self.songs.remove(song)
                removed = True
        if not removed:
            print("No song removed, try different parameters.")
        