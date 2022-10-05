from django.forms import ModelForm
from .models import Song

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['artist_id', 'album_id', 'title', 'track_number', 'length', 'disc_number']
