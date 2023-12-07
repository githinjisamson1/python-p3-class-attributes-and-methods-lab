class Song:
    name = None
    artist = None
    genre = None
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    
    def __init__(self, name, artist, genre):
        Song.add_song_count()
        Song.updateName(name)
        Song.updateArtist(artist)
        Song.updateGenre(genre)
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        
    
    @classmethod
    def updateName(cls, name):
        cls.name=name
        
    @classmethod
    def updateArtist(cls, artist):
        cls.artist=artist
        
    @classmethod   
    def updateGenre(cls, genre):
        cls.genre=genre
        
    @classmethod
    def add_song_count(cls):
        cls.count +=1
        
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            
    @classmethod
    def add_to_genre_count(cls, genre):
        # for genre in cls.genres:
            if genre not in cls.genre_count:
                cls.genre_count.update({genre: 1})
            else:
                cls.genre_count[genre] += 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        # for artist in cls.artists:
            if artist not in cls.artist_count:
                cls.artist_count.update({artist: 1})
            else:
                cls.artist_count[artist] += 1
        
      


song1 = Song("Haufananishwi", "Boaz Dunken", "Gospel")
song2 = Song("Haufananishwi", "Boaz Dunken", "Gospel")
song3 = Song("ABC", "John Doe", "Lofi")
song4 = Song("ABC", "John Doe", "Lofi")
song5 = Song("ABC", "John Doe", "Lofi")

print(Song.name)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)
print(Song.count)
print(song1.name)