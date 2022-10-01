"""
Populate c-tunes database users_songs table with fake data using the django ORM.
"""

import random
from django.contrib.auth.models import User
from songs.models import Song, Users_Songs

song_id_list = []
song_id_list = Song.objects.filter().values_list('pk', flat=True)

user_id_list = []
user_id_list = User.objects.filter().values_list('pk', flat=True)

USER_COUNT = user_id_list.count()
SONG_COUNT = song_id_list.count()
USER_SONGS_COUNT = 120

assert USER_SONGS_COUNT <= (USER_COUNT * SONG_COUNT)

print (song_id_list)
print (user_id_list)
print (USER_COUNT, SONG_COUNT)



def main():
    """Main driver function"""
    app = create_app()
    app.app_context().push()
    truncate_tables()


    user_song_pairs = set()
    while len(user_song_pairs) < USER_SONGS_COUNT:

        candidate = (
            random.randint(13, 15),
            random.randint(77, 152)
        )


        """
        need to edit to get the min and max id from each table to set the random limits
        """

        if candidate in  user_song_pairs:
            continue  # pairs must be unique

        user_song_pairs.add(candidate)

    new_song = [{"user_id": pair[0], "song_id": pair[1]} for pair in list( user_song_pairs)]
    insert_likes_query = users_songs.insert().values(new_song)
    db.session.execute(insert_likes_query)

    # insert likes
    db.session.commit()


# run script
main()
