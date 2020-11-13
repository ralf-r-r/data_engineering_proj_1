# Data Modeling with Postgres
This projects implements an ETL pipeline to transfers data from files in tables in Postgres using Python and SQL.
The project defines fact and dimension tables for a star schema for a particular analytic focus.

# Porject Structure
- **sql_queries.py**: Contains the SQL statements for: create tables, drop tables, insert values
- **etl.py**: Contains the python code to process an entire directory of json files
- **create_tables.py**: Cotains the python code to create the tables

# Data Set and Tables
The data consists of a song and a log data set for song play analysis. The ```create_table.py``` script creates the following tables:

### Fact Tables
**songplay** - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
- **users** - users in the app
user_id, first_name, last_name, gender, level

- **songs** - songs in music database
song_id, title, artist_id, year, duration

- **artists** - artists in music database
artist_id, name, location, latitude, longitude

- **time** - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday


# How to run the code

### Create the tables
Run the following command in the terminal
```
python create_tables.py
```

### Insert data from json files
Run the following command in the terminal
```
python etl.py
```
