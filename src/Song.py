

class Song:
    name: str
    artist: str
    duration: str
    votes: int

    def __init__(self, name, artist, duration, votes):
        self.name = name
        self.artist = artist
        self.duration = int(duration)
        self.votes = int(votes)

    def __str__(self):
        return f"{self.name} | {self.artist} | duration: {self.msToMin()} | {self.votes} votes."

    def msToMin(self):
        ms = self.duration
        seconds, ms = divmod(ms, 1000)
        minutes, seconds = divmod(seconds, 60)
        return(f'{int(minutes):01d}:{int(seconds):02d}')

    def vote(self):
        self.votes += 1

    def unvote(self):
        self.votes -= 1


    