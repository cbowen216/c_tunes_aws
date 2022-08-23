from rest_framework import serializers
from albums.models import Album
from artists.models import Artist
from songs.models import Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('__all__')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'track_number', 'length', 'disc_number', 'artist_id', 'album_id')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'year_released', 'track_count', 'disc_count', 'artist_id')