

'''
class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def name_and_address(self):
        return(self.name + 'lives in ' + self.address)

student1 = Student('Flavio', 'Toronto')
student2 = Student('Marcus', 'Guelph')

print(student1.address)
print(student1.name_and_address())
'''
from random import randint
class Playlist:
    def __init__(self):
        self.playlist = []
    
    def add_to_playlist(self, song):
        self.playlist.append(song)

    def remove_from_playlist(self, id):
        #you need to access the index of the item for it to be removed
        for idx, song in enumerate(self.playlist):
            if song['id'] == id:
                self.playlist.pop(idx)

    def get_songs(self):
        for song in self.playlist:
            print('{} - by {}'.format(song['title'], song['artist']))
    
    def size(self):
        return len(self.playlist)

    def shuffle(self):
        for idx, song in enumerate(self.playlist):
            shuffle_idx = randint(0,len(self.playlist)-1)
            self.playlist[idx],self.playlist[shuffle_idx] = self.playlist[shuffle_idx],self.playlist[idx]
        
        pass


my_songs = Playlist()
my_songs.add_to_playlist({'id': 10, 'title': 'Passionfruit', 'artist': 'Drake'})
my_songs.add_to_playlist({'id': 20, 'title': 'Sup', 'artist': 'Word'})
my_songs.add_to_playlist({'id': 30, 'title': 'Yeah', 'artist': 'Usher'})
my_songs.add_to_playlist({'id': 40, 'title': 'After Party', 'artist': 'Koffee Brown'})
my_songs.add_to_playlist({'id': 50, 'title': 'Lets get it On', 'artist': 'Marvin Gaye'})



my_songs.get_songs()
my_songs.shuffle()
my_songs.get_songs()

