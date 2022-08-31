import json
from albums.models import Album
from artists.models import Artist

with open('Album_seed_data.json') as f:
    album_json = json.load(f)

for album in album_json:
    album = Album(title=album['title'], year_released=album['year_released'], track_count=album['track_count'], disc_count=album['disc_count'], artist_id=Artist.objects.get(id=album['artist_id']))

    album.save()
    