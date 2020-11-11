# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = (""" 
CREATE TABLE IF NOT EXISTS
songplay (
    songplay_id varchar,start_time int,user_id varchar,
    level varchar, song_id varchar, artist_id varchar, 
    session_id int, location varchar, user_agent varchar
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS
user_table(
    user_id varchar, first_name varchar, last_name varchar, 
    gender varchar, level varchar
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS
song_table(
    song_id varchar, title varchar, artist_id varchar, 
    year int, duration float
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS
artist_table(
    artist_id varchar, name varchar, location varchar, latitude float, longitude float
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS
time_table(
    start_time int, hour int, day int, week int, month int, year int, weekday int
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]