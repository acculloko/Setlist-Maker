from src.Song import Song

class Setlist:
    songs: [Song]

    def __init__(self):
        self.songs = []

    def show(self):
        time = 0
        print("\nSetlist:\n")
        for song in sorted(self.songs, key=lambda x: x.votes, reverse=True):
            print(f"{song}\n")
            time += song.duration
        print(f"{len(self.songs)} total songs, with a total time of {self.msToMin(time)}.")

    def findByName(self, name):
        counter = 0
        for song in self.songs:
            if name in song.name:
                print(f"{song}\n")
                counter += 1
                time += song.duration
        print(f"{counter} songs found, with a total of {self.msToMin(time)}.")

    def findByArtist(self, artist):
        counter = 0
        for song in self.songs:
            if artist in song.artist:
                print(f"{song}\n")
                counter += 1
                time += song.duration
        print(f"{counter} songs found, with a total of {self.msToMin(time)}.")

    def findByVotes(self, votes):
        counter = 0
        time = 0
        for song in self.songs:
            if song.votes == votes:
                print(f"{song}\n")
                counter += 1
                time += song.duration
        print(f"{counter} songs found, with a total of {self.msToMin(time)}.")

    def msToMin(self, time):
        ms = time
        seconds, ms = divmod(ms, 1000)
        minutes, seconds = divmod(seconds, 60)
        return(f'{int(minutes):01d}:{int(seconds):02d}')

    def add(self, Song):
        self.songs.append(Song)
        print(f"Added {Song.name} to setlist.")

    def remove(self, name, artist):
        removed = False
        for song in self.songs:
            if song.name == name and song.artist == artist:
                print(f"Removing {song.name}...")
                self.songs.remove(song)
                removed = True
        if not removed:
            print("No song removed, try different parameters.")
        