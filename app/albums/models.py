from django.db import models
from artists.models import Artist

class Album(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    year_released = models.PositiveSmallIntegerField(blank=False, default='')
    track_count = models.PositiveSmallIntegerField('Total Number of Tracks', blank=True, default='')
    disc_count = models.PositiveSmallIntegerField('Total Number of Discs', blank=True, default='')
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)