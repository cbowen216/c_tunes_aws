from django.db import models
from artists.models import Artist
from albums.models import Album
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    length = models.TimeField(blank=True, default='0:00')
    track_number = models.PositiveSmallIntegerField(blank=True, default=0)
    disc_number = models.PositiveSmallIntegerField(blank=True, default=0)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)

