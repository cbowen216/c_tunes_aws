from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, blank=False, default='')

    def __str__(self) -> str:
        return f'{self.name}'
