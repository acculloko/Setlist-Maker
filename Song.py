

class Song:
    name: str
    artist: str
    duration: str
    votes: int

    def __init__(self, name, artist, duration, votes):
        self.name = name
        self.artist = artist
        self.duration = duration
        self.votes = votes

    def __str__(self):
        return f"{self.name} - {self.artist}: {self.votes} votes."

    def vote(self):
        self.votes += 1

    def unvote(self):
        self.votes -= 1


    