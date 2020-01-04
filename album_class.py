class Track:
    def __init__(self, artist, title, album=None):
        self.artist = str(artist)
        self.title = str(title)
        self.album = album

    def __str__(self):
        return self.artist + ", " + self.title + ", " + self.album

    def set_album(self, album):
        self.album = album

artist = input("Enter the artist: ")
title = input("Enter the song title: ")
album = input("Enter the album: ")

my_track = Track(artist, title, album)
print(my_track)
