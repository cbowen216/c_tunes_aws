from django.db import models
from artists.models import Artist
from albums.models import Album
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    track_number = models.PositiveSmallIntegerField(blank=True, default=0)
    length = models.CharField(max_length=10, blank=True, default='')
    disc_number = models.PositiveSmallIntegerField(blank=True, default=0)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'

# Many to many relational table between Users and songs
class Users_Songs(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
