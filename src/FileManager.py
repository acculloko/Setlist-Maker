# reads and writes CSV files for persistency
import csv, os, re, spotipy
from src.Song import Song
from src.Setlist import Setlist
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

class FileManager:

    def read(self, path):
        songs = []

        if not os.path.exists(path):
            file = open(path, 'w')
            file.close()

        with open(path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                songs.append(Song(row[0], row[1], row[2], row[3]))
        
        return songs

    def write(self, setlist: Setlist, path):
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            for song in setlist.songs:
                writer.writerow([song.name, song.artist, song.duration, song.votes])

    def writeSpotify(self, link, path):
        load_dotenv()

        CLIENT_ID = os.getenv("CLIENT_ID", "")
        CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
        OUTPUT_FILE_NAME = path

        # auth
        client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # get list of tracks in a given playlist (note: max playlist length 100)
        tracks = session.playlist_tracks(link)["items"]

        # create csv file
        with open(OUTPUT_FILE_NAME, "w", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)

            # extract name and artist
            for track in tracks:
                name = track["track"]["name"]
                artists = ", ".join(
                    [artist["name"] for artist in track["track"]["artists"]]
                )
                duration = track["track"]["duration_ms"]

                # write to csv
                writer.writerow([name, artists, int(duration), int(0)])


