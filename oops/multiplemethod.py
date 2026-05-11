class playlist :
    def __init__(self,name):
        self.name = name
        self.songs = []
    
    def add_Song(self,song):
        self.songs.append(song)
        print(f"Added : {song}")
    
    def remove_song(self,song):
        self.songs.remove(song)
        print(f"Removed : {song}")
    
    def show_songs(self):
        for song in self.songs:
            print(song)
    
myplaylist = playlist("Saimon's Playlist")
myplaylist.add_Song("That should be me")
myplaylist.add_Song("One less lonely girl")
myplaylist.add_Song("The man who cant be moved on")
myplaylist.show_songs()
myplaylist.remove_song("One less lonely girl")
myplaylist.show_songs()