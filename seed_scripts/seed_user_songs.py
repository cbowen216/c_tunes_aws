"""
Populate twitter database with fake data using the SQLAlchemy ORM.
this will not work if you had rewriten the data
"""

import random
from src.models import users_songs, db
from src import create_app

USER_COUNT = 3
SONG_COUNT = 76
USER_SONGS_COUNT = 120

assert USER_SONGS_COUNT <= (USER_COUNT * SONG_COUNT)



def truncate_tables():
    """Delete all rows from database tables"""
    db.session.execute(users_songs.delete())
    db.session.commit()


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

"""
save for later

#random.randint(last_user.id - USER_COUNT + 1, last_user.id),

"""
