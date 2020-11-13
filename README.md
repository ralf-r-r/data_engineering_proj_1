# Data Modeling with Postgres
This projects implements an ETL pipeline to transfers data from files in tables in Postgres using Python and SQL.
The project defines fact and dimension tables for a star schema for a particular analytic focus.

# Porject Structure
- **sql_queries.py**: Contains the SQL statements for: create tables, drop tables, insert values
- **etl.py**: Contains the python code to process an entire directory of json files
- **create_tables.py**: Cotains the python code to create the tables

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
