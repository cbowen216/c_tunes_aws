import json
from datetime import datetime
from songs.models import Song
from albums.models import Album
from artists.models import Artist

with open('Song_seed_data.json') as f:
    song_json = json.load(f)

format_data = "%M:%S"

for song in song_json:
    song = Song(
        title=song['title'],
        track_number=song['track_number'],
        length=song['length'], 
        disc_number=song['disc_number'], 
        album_id=Album.objects.get(id=song['album_id']),
        artist_id=Artist.objects.get(id=song['artist_id']))

    song.save()