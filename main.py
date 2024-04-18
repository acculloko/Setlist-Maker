from Song import Song
from Setlist import Setlist
from FileManager import FileManager

path = "./data/setlist.csv"
endCondition = True
firstLoop = True

fileManager = FileManager()
setlist = Setlist()

songsFromCsv = fileManager.read(path)
if len(songsFromCsv) > 0:
    for s in songsFromCsv:
        setlist.add(s)

# setlist.add(Song("Videogame", "Projota", 23456, 0))
# setlist.remove("Videogame", "Projota")

# Main loop
while(endCondition):
    # User interface
    if firstLoop:
        print("\nWelcome to the setlist maker!")
        firstLoop = False
    else:
        print("")
    print("find - Find songs;")
    print("add - Add a song;")
    print("remove - remove a song;")
    print("vote - add a vote to a song")
    print("exit - exit application;\n")
    choice = input("Make your choice: ")

    if choice == "find":
        print("all - Show full setlist;")
        print("name - Find by name;")
        print("artist - Find by artist;")
        print("votes - Find by votes;")
        print("back - Return;\n")
        find_choice = input("Make your choice: ")

        if find_choice == "all":
            setlist.show()

        elif find_choice == "name":
            find_name = input("Enter song name: ")
            print()
            setlist.findByName(find_name)

        elif find_choice == "artist":
            find_artist = input("Enter artist: ")
            print()
            setlist.findByArtist(find_artist)

        elif find_choice == "votes":
            find_votes = int(input("Enter votes: "))
            print()
            setlist.findByVotes(find_votes)

    elif choice == "add":
        name = input("Enter song name: ")
        artist = input("Enter artist: ")
        duration = input("Enter duration: ")

        setlist.add(Song(name, artist, duration, 0))

    elif choice == "remove":
        name = input("Enter song name: ")
        artist = input("Enter artist: ")

        setlist.remove(name, artist)

    elif choice == "vote":
        voted = False
        name = input("Enter song name: ")

        for song in setlist.songs:
            if name in song.name:
                song.vote()
                voted = True
                print(f"Added a vote to {song.name}, for a total of {song.votes} votes.")
        if not voted:
            print("Song not found!")

    elif choice == "unvote":
        unvoted = False
        name = input("Enter song name: ")

        for song in setlist.songs:
            if name == song.name:
                song.unvote()
                unvoted = True
                print(f"Removed a vote from {song.name}, for a total of {song.votes} votes.")
        if not unvoted:
            print("Song not found!")

    elif choice == 'import_playlist':
        if input("This will overwrite all saved data! Proceed? (Y/N) ") == "Y":
            fileManager.writeSpotify("0sqD0L7sB7l7GrVUFNGA4H", path)

            songsFromCsv = fileManager.read(path)
            if len(songsFromCsv) > 0:
                for s in songsFromCsv:
                    setlist.add(s)

    elif choice == "exit":
        endCondition = False

# End loop

fileManager.write(setlist, path)