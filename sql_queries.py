# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = (""" 
CREATE TABLE IF NOT EXISTS
songplay_table (
    songplay_id SERIAL PRIMARY KEY NOT NULL,start_time varchar NOT NULL ,user_id varchar NOT NULL,
    level varchar NOT NULL, song_id varchar, artist_id varchar, 
    session_id varchar, location varchar, user_agent varchar
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS
user_table(
    user_id VARCHAR PRIMARY KEY NOT NULL, first_name varchar NOT NULL, last_name varchar NOT NULL, 
    gender varchar, level varchar NOT NULL
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS
song_table(
    song_id VARCHAR PRIMARY KEY NOT NULL, title varchar NOT NULL, artist_id varchar NOT NULL, 
    year int, duration float
)
""")


artist_table_create = ("""
CREATE TABLE IF NOT EXISTS
artist_table(
    artist_id VARCHAR PRIMARY KEY NOT NULL, name varchar NOT NULL, location varchar, latitude float, longitude float
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS
time_table(
    start_time VARCHAR PRIMARY KEY NOT NULL, hour int NOT NULL, day int NOT NULL, week int NOT NULL, month int NOT NULL, year int NOT NULL, weekday int NOT NULL
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay_table(start_time, user_id, level, song_id, 
artist_id, session_id, location, user_agent) VALUES(%s, %s, %s, %s, %s ,%s, %s ,%s)
""")

user_table_insert = ("""
INSERT INTO user_table(user_id, first_name, last_name, 
gender, level) VALUES(%s, %s, %s, %s ,%s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO song_table(song_id, title, artist_id, 
year, duration) VALUES(%s, %s, %s, %s ,%s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artist_table(artist_id, name, location, 
latitude, longitude) VALUES(%s, %s, %s, %s ,%s)
ON CONFLICT DO NOTHING
""")

time_table_insert = ("""
INSERT INTO time_table(start_time, hour, day, week, 
month, year, weekday) VALUES(%s, %s, %s, %s ,%s, %s, %s)
ON CONFLICT DO NOTHING
""")


# FIND SONGS

song_select = ("""
SELECT  song_table.song_id, artist_table.artist_id
FROM song_table
INNER JOIN artist_table ON song_table.artist_id = artist_table.artist_id
WHERE song_table.title = %s
AND artist_table.name = %s
AND song_table.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]