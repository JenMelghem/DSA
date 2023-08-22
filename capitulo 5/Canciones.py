from LinkStack import LinkStack


class song(object):
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
    
    def __str__(self):
        return f"{self.title} by {self.artist}"
    
playlist = LinkStack()

playlist.push(song("As it Was", "Harry Styles"))
playlist.push(song("Te amo", "Makano"))
playlist.push(song("Home", "One Direction"))
playlist.push(song("Torero", "Chayanne"))

print("Playlist:")
print(playlist)

actual_song = playlist.peek()
print("En reproducción:")
print(actual_song)
print("1:30━━━━●───────── 3:17")

print("Reproducir otra cancion >")
input()

playlist.pop()
print("En reproducción:")
print(actual_song)
print("1:30━━━━●───────── 3:17")