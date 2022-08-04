-- portfolio project -- Chris Bowen
--SQL Script to create and populate my datbase
--if database already exists this WILL 
--ERASE any changes and set back to a defaultstate

-- use the following in the termainal to run this script

'''

cat ctunes_creation_script.sql | docker exec -i pg_container psql

'''
-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'c_tunes' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS c_tunes;
CREATE DATABASE c_tunes;
-- connect via psql
\c c_tunes

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

---
--- CREATE tables
---

CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE songs(
    song_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    length TEXT,
    track_number INT,
    disc_number INT,
    written_by INT,
    track_of INT
);

CREATE TABLE users_songs(
    user_id INT,
    song_id INT,
    PRIMARY KEY (user_id, song_id)
);

CREATE TABLE artists(
    artist_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE albums (
    album_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    year INT,
    cover_art TEXT,
    total_discs INT,
    released_by INT
);

---
--- Add foreign key constraints
---

ALTER TABLE users_songs
ADD CONSTRAINT fk_users_songs_user 
FOREIGN KEY (user_id) 
REFERENCES users (id);

ALTER TABLE users_songs
ADD CONSTRAINT fk_users_songs_song 
FOREIGN KEY (song_id) 
REFERENCES songs (id);

ALTER TABLE songs
ADD CONSTRAINT fk_songs_written_by 
FOREIGN KEY (written_by) 
REFERENCES artists (id);

ALTER TABLE songs
ADD CONSTRAINT fk_songs_album
FOREIGN KEY (track_of) 
REFERENCES albums (id);

ALTER TABLE albums
ADD CONSTRAINT fk_albums_artist
FOREIGN KEY (released_by) 
REFERENCES artists (id);

-- add some data 

-- Users
INSERT INTO users (email, password)
VALUES ('chris@chris.com', 'password123');

INSERT INTO users (email, password)
VALUES ('you@domain.com', 'password');

INSERT INTO users (email, password)
VALUES ('other@place.com', 'mypassword');


-- Users
INSERT INTO users (email, password)
VALUES ('chris@chris.com', 'password123');

INSERT INTO users (email, password)
VALUES ('you@domain.com', 'password');

INSERT INTO users (email, password)
VALUES ('other@place.com', 'mypassword');


-- artists
INSERT INTO artists (name)
VALUES ('Metallica');

INSERT INTO artists (name)
VALUES('Pink Floyd');

INSERT INTO artists (name)
VALUES('Beatles');

INSERT INTO artists (name)
VALUES('Missy Elliot');


-- add albums
INSERT INTO albums (title, year, total_discs)
VALUES('The Wall', 1979, 2);

UPDATE albums
SET released_by = (SELECT id FROM artists WHERE name = 'Pink Floyd')
WHERE title = 'The Wall';

INSERT INTO albums (title, year, total_discs, released_by)
    (SELECT 'Animals', 1977, 1, id 
        FROM artists 
        WHERE name = 'Pink Floyd');

INSERT INTO albums (title, year, total_discs, released_by)
    (SELECT 'Master of Puppets', 1986, 1, id
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO albums (title, year, total_discs, released_by)
    (SELECT 'Ride the Lightning', 1984, 1, id
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO albums (title, year, total_discs, released_by)
    (SELECT 'Let It Be', 1968, 1, id
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO albums (title, year, total_discs, released_by)
    (SELECT 'Supa Dupa Fly', 1997, 1, id
        FROM artists
        WHERE name = 'Missy Elliot');


-- add songs 
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'In The Flesh?', '3:20', 1, 1, id, 
        (SELECT id 
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'The Thin Ice', '2:27', 2, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Another Brick in the Wall, Part 1', '3:11', 3, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');
        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'The Happiest Days of Our Lives', '1:46', 4, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');
        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Another Brick in the Wall, Part 2', '3:59', 5, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');
        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Mother', '5:32', 6, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Goodbye Blue Sky', '2:45', 7, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Empty Spaces', '2:10', 8, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Young Lust', '3:25', 9, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'One of My Turns', '3:41', 10, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Dont Leave Me Now', '4:08', 11, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Another Brick in the Wall, Part 3', '1:18', 12, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Goodbye Cruel World', '1:16', 13, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Hey You', '4:40', 1, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Is There Anybody Out There?', '2:44', 2, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Nobody Home', '3:26', 3, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');
        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Vera', '1:35', 4, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');
        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Bring the Boys Back Home', '1:21', 5, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');
        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Comfortably Numb', '6:32', 6, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'The Show Must Go On', '1:36', 7, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

        
INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'In The Flesh', '4:15', 8, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Run Like Hell', '4:20', 9, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Waiting for the Worms', '4:04', 10, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Stop', '0:30', 11, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'The Trial', '5:13', 12, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Outside the Wall', '1:41', 13, 2, id, 
        (SELECT id
        FROM albums
        WHERE title = 'The Wall'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Pigs on the Wing (Part 1)', '1:24', 1, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'Animals'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Dogs', '17:04', 2, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'Animals'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Pigs (Three Different Ones)', '11:28', 3, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'Animals'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Sheep', '10:20', 4, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'Animals'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs (title, length, track_number, 
disc_number, written_by, track_of)
    (SELECT 'Pigs on the Wing (Part 2)', '1:24', 5, 1, id, 
        (SELECT id
        FROM albums
        WHERE title = 'Animals'
        ) FROM artists
        WHERE name = 'Pink Floyd');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Battery', '5:13', 1, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Master of Puppets')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Master of Puppets', '8:36', 2, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Master of Puppets')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'The Thing That Should Not Be', '6:36', 3, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Master of Puppets')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Welcome Home (Sanitarium)', '6:27', 4, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Master of Puppets')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Disposable Heros', '8:17', 5, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Master of Puppets')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Leper Messiah', '5:40', 6, 1,id,
        (SELECT id
        FROM albums
        WHERE title = 'Master of Puppets')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Orion', '8:27', 7, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Master of Puppets')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Damage, Inc.', '5:32', 8, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Master of Puppets')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Fight Fire with Fire', '4:44', 1, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Ride the Lightning')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Ride the Lightning', '6:37', 2, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Ride the Lightning')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'For Whom the Bell Tolls', '5:11', 3, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Ride the Lightning')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Fade to Black', '6:55', 4, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Ride the Lightning')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Trapped Under Ice', '4:04', 5, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Ride the Lightning')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Escape', '4:24', 6, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Ride the Lightning')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Creeping Death', '6:36', 7, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Ride the Lightning')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'The Call of Ktulu', '8:55', 8, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Ride the Lightning')
        FROM artists
        WHERE name = 'Metallica');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Two of Us', '3:36', 1, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Dig a Pony', '3:54', 2, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Across the Universe', '3:48', 3, 1, id,
        (SELECT id
        FROM albums
        WHERE title ='Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'I Me Mine', '2:26', 4, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Dig It', '0:50', 5, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Let It Be', '4:03', 6, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Maggie Mae', '0:40', 7, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Ive Got a Feeling', '3:37', 8, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'One After 909', '2:45', 9, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'The Long and Winding Road', '3:38', 10, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'For You Blue', '2:32', 11, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Get Back', '3:09', 12, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Let It Be')
        FROM artists
        WHERE name = 'Beatles');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Bustas Intro', '1:53', 1, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Hit Em wit da Hee', '4:19', 2, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Sock It 2 Me', '4:17', 3, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'The Rain (Supa Dupa Fly)', '4:11', 4, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Beep Me 911', '4:57', 5, 1, id,
        (SELECT id
        FROM albums
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'They Dont Wanna Fuck wit Me', '3:18', 6, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Pass da Blunt', '3:17', 7, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Bite Our Style (Interlude)', '0:43', 8, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Friendly Skies', '4:11', 9, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Best Friends', '4:07', 10, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Dont Be Commin (In My Face)', '4:11', 11, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Izzy Izzy Ahh', '3:54', 12, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Why You Hurt Me', '4:31', 13, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Im Talkin', '5:02', 14, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Gettaway', '4:25', 15, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Bustas Outro', '1:38', 16, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');

INSERT INTO songs(title, length, track_number, disc_number, written_by, track_of)
    (SELECT 'Missys Finale', '0:24', 17, 1, id,
        (SELECT id
        FROM albums 
        WHERE title = 'Supa Dupa Fly')
        FROM artists
        WHERE name = 'Missy Elliot');
