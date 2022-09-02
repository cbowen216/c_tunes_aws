from django import forms
from .models import Artist


class NewArtistForm(forms.forms):
    name = forms.CharField()