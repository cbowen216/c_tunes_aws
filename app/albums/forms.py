from django.forms import ModelForm
from .models import Album

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['artist_id', 'title', 'disc_count', 'track_count', 'year_released']