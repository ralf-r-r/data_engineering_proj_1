import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    processes a single song file and inserts data 
    into the song_table and artist_table
    
    :param cur: psycopg2.extensions.cursor
    :param filepath: str, path to a single json file
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    selectedColumns = ["song_id", "title", "artist_id", "year", "duration"]
    song_data = list(df[selectedColumns].values[0])
    cur.execute(song_table_insert, song_data)

    # insert artist record
    selectedColumns = ["artist_id", "artist_name",
                       "artist_location", "artist_latitude", "artist_longitude"]
    artist_data = list(df[selectedColumns].values[0])
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    processes a single log file and inserts data 
    into time_table, user_table and songplay_table

    :param cur: psycopg2.extensions.cursor
    :param filepath: str, path to a single json file
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df["page"] == "NextSong"]

    # convert timestamp column to datetime
    t = pd.to_datetime(df["ts"], unit='ms')

    # insert time data records
    pdSeries = dict(
        start_time=t,
        hour=t.dt.hour,
        day=t.dt.day,
        weekofyear=t.dt.weekofyear,
        month=t.dt.month,
        year=t.dt.year,
        weekday=t.dt.weekday)

    time_df = pd.DataFrame(pdSeries)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    selectedColumns = ["userId", "firstName", "lastName", "gender", "level"]
    user_df = df[selectedColumns]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = [str(row.ts),
                         row.userId,
                         row.level,
                         songid,
                         artistid,
                         str(row.sessionId),
                         row.location,
                         row.userAgent]

        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    processes all json files in filepath and
    inserts data into song_table, artist_table, time_table, 
    user_table and songplay_table

    :param cur: psycopg2.extensions.cursor
    :param conn: psycopg2.extensions.connection
    :param filepath: str, path to a single json file
    :param func: function
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
