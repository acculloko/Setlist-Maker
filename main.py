from Song import Song
from Setlist import Setlist
from FileManager import FileManager

endCondition = True

fileManager = FileManager("./setlist.csv")

setlist = Setlist()

songsFromCsv = fileManager.read()
if len(songsFromCsv) > 0:
    for s in songsFromCsv:
        setlist.add(s)

# setlist.add(Song("Videogame", "Projota", "2:40", 0))
# setlist.remove("Videogame", "Projota")

setlist.show()

while(endCondition):
    # implement UI
    pass

fileManager.write(setlist)