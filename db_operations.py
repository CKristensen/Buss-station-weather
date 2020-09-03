import psycopg2
from psycopg2 import sql
import getpass 
import os

PASS = os.environ['ACADEMY_DB_PASS']
USER = os.environ['ACADEMY_USER_NAME']
DBNAME = 'team_ccm'
HOST = os.environ['ACADEMY_DB']


def connect():
    """Connects to postgresdatabase

    Args:
        dbname (string): name of your catalog
        user (string): name of your username
        password (password): your password

    Returns:
        [type]: [description]

    """    
    conn = psycopg2.connect(host = "ds-etl-academy.cgbivchwjzle.eu-west-1.rds.amazonaws.com",
    dbname = DBNAME,
    user = USER,
    password = PASS,
    port = 5432
    )
    cursor = conn.cursor()
    return conn, cursor

def close(conn, cursor):  
    #closes connection to database
    conn.commit()
    cursor.close()
    conn.close()

def create_table_weather_station():
	conn, cur = connect()
	table = '''CREATE TABLE IF NOT EXISTS frostentur.weatherStationLatLon (sourceId text primary key,
	name text,
	lat float,
	lon float);'''
	cur.execute(table)
	
	table = '''CREATE TABLE IF NOT EXISTS frostentur.weatherStationTemperatures(sourceId text,
	date int,
	referenceTime text,
	value float,
	unit text);'''
	cur.execute(table)

	table = '''CREATE TABLE IF NOT EXISTS frostentur.busStopRoute(route_id int,
		stop_id int);'''
	cur.execute(table)

	table = '''CREATE TABLE IF NOT EXISTS frostentur.busStopLatLon(stop_id int, stop_name text,
	lat float,
	lon float
	);'''
	cur.execute(table)


	close(conn, cur)

# def create_data_mart():
# 	CREATE TABLE IF NOT EXISTS datamart_star.route (
#     route_id int primary key,
#     route_long_name text,
#     route_short_name text,
#     type text
# );

# CREATE TABLE IF NOT EXISTS datamart_star.buss_stopp (
#     bkey text primary key,
#     buss_stopp_id int,
#     buss_stopp_name text,
#     latitude float,
#     longitude float

# );

# CREATE TABLE IF NOT EXISTS datamart_star.route_busstop (
#     bkey text primary key references buss_stopp(bkey),
#     route_id int referencesroute(route_id)
# );

# CREATE TABLE IF NOT EXISTS datamart_star.weatherstation_s (
#     sourceid text primary key,
#     name text,
#     latitude float,
#     longitude float
# )

# CREATE TABLE IF NOT EXISTS datamart_star.facttable (
#     skey serial primary key,
#     buss_stop_id text references buss_stopp(bkey),
#     sourceid text references weatherstation_s(sourceId),
#     ktime int references times(ktime),
#     kdate int references date_s(k_date)
# )



create_table_weather_station()