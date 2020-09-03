# Buss-station-weather
Getting the weather reports for each buss station using FrostAPi and Entur.

To run the program please edit the following lines in the program.

FILE:db_operations.py

  PASS = os.environ['ACADEMY_DB_PASS']
  USER = os.environ['ACADEMY_USER_NAME']
  DBNAME = 'team_ccm'
  HOST = os.environ['ACADEMY_DB']
change the following to your database details.

FILE:main.py

  CLIENT_ID = os.environ['FROST_API_CLIENT_ID']
with your frostapi client id (https://frost.met.no/howto.html)

Project still in progress.
At this moment what it does:
  - Gets the weather for all buss stations in Oslo of yesterday.
  - Display in the command line the buss station with highest temperature per route.
  - Uncomment the line create_db() in the main.py in order to create a new database.
