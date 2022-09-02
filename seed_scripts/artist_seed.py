import json
from artists.models import Artist

with open('Artist_seed_data.json') as f:
    artist_json = json.load(f)

for artist in artist_json:
    artist = Artist(name=artist['name'])

    artist.save()
    