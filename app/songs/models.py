import imp
from tkinter import CASCADE
from django.db import models
from artists.models import Artist
from albums.models import Albums

class Songs(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    length = models.TimeField(blank=True, default='')
    track_number = models.PositiveSmallIntegerField(max_length=3, blank=True, default='')
    disc_number = models.PositiveSmallIntegerField(max_length=3, blank=True, default='')
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Albums, on_delete=models.CASCADE)

