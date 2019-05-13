from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} -- {self.singer}'

    def serialize(self):
        song_list = []
        for song in self.song_set.all():
            song_list.append(song.serialize_simple())
        
        return {
            'name': self.name,
            'singer': self.singer,
            'songs': song_list
        }

    @staticmethod
    def get_all():
        album_list = []
        for album in Album.objects.all():
            album_list.append(album.serialize())     
        return album_list
   
   
class Song(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def serialize_simple(self):        
        return {
            'name': self.name,
            'genre': self.genre,
            'timestamp': self.timestamp.strftime('%B %d,%Y %H:%M %p')
        }
    
