# reads and writes CSV files for persistency
import csv, os
from Song import Song
from Setlist import Setlist

class FileManager:
    path: str

    def __init__(self, path):
        self.path = path


    def read(self):
        songs = []

        if not os.path.exists(self.path):
            file = open(self.path, 'w')
            file.close()

        with open(self.path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                songs.append(Song(row[0], row[1], row[2], row[3]))
        
        return songs

    def write(self, setlist: Setlist):
        with open(self.path, 'w', newline='') as f:
            writer = csv.writer(f)
            for song in setlist.songs:
                writer.writerow([song.name, song.artist, song.duration, song.votes])

    def setPath(self, path):
        self.path = path