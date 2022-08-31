from django.db import models
from artists.models import Artist


class Album(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    year_released = models.PositiveSmallIntegerField(blank=False, default=0)
    track_count = models.PositiveSmallIntegerField('Total Number of Tracks', blank=True, default=0)
    disc_count = models.PositiveSmallIntegerField('Total Number of Discs', blank=True, default=0)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'
