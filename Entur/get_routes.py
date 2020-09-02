import requests
import os
from zipfile import ZipFile 
import pandas as pd

def get_en_tur_data():
    '''


    Returns: Dataframe with route_id and stop_id columns

    '''
    url = 'https://storage.googleapis.com/marduk-production/outbound/gtfs/rb_rut-aggregated-gtfs.zip'

    myfile = requests.get(url)

    current_folder = os.getcwd()

    open(current_folder+'/routes.zip', 'wb').write(myfile.content)
    stops = pd.DataFrame()
    routes = pd.DataFrame()

    with ZipFile('routes.zip') as myzip:
        with myzip.open('stops.txt') as myfile1:
            stops = pd.read_csv(myfile1)
        with myzip.open('routes.txt') as myfile2:
            routes = pd.read_csv(myfile2)
        with myzip.open('trips.txt') as myfile3:
            trips = pd.read_csv(myfile3)
        with myzip.open('stop_times.txt') as myfile4:
            stop_times = pd.read_csv(myfile4)

    # stops = stops[['stop_id', 'stop_name', 'stop_lat', 'stop_lon']]
    # routes = routes[['route_id', 'route_short_name', 'route_long_name', 'route_type']]
    trips = trips[['trip_id', 'route_id']]
    # stop_times = stop_times[['trip_id', 'stop_id']]

    # df_ = pd.merge(stop_times, trips, on='trip_id', how='inner')
    # df_ = df_.drop_duplicates()

    # return (df_[['route_id', 'stop_id']])
    return  trips


print(get_en_tur_data())