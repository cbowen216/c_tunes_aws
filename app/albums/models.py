from django.db import models
from artists.models import Artist

class Albums(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    year_released = models.PositiveSmallIntegerField(max_length=4, blank=False, default='')
    track_count = models.PositiveSmallIntegerField('Total Number of Tracks', max_length=3, blank=True, default='')
    disc_count = models.PositiveSmallIntegerField('Total Number of Discs', max_length=3, blank=True, default='')
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

