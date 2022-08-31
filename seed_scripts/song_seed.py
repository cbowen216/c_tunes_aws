import json
from songs.models import Songs
from albums.models import Album
from artists.models import Artist

with open('Song_seed_data.json') as f:
    song_json = json.load(f)

for song in song_json:
    song = Song(
        title=song['title'],
        track_number=song['track_number'],
        length=song['length'], 
        disc_number=song['disc_number'], 
        track_of=Album.object.get(id=song['track_of']),
        artist_id=Artist.objects.get(id=song['artist_id']))

    #song.save()