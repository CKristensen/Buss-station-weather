import requests
import re
import pandas as pd
import os

# Insert your own client ID here
CLIENT_ID = os.environ['FROST_API_CLIENT_ID']

def get_weather_station_latlon():
    """Goes into FrostAPI and gets all the stations unique SN 
    numbers in Oslo, their names and their coordinates.
    returns: pandas Dataframe with columns 'id', 'name', 'lat', 'lon': 
    """    
    # Define endpoint and parameters
    endpoint = 'https://frost.met.no/sources/v0.jsonld'
    parameters = {
        'county': 'Oslo'
    }
    # Issue an HTTP GET request
    r = requests.get(endpoint, parameters, auth=(CLIENT_ID,''))
    # Extract JSON data
    json = r.json()
    
    # Check if the request worked, print out any errors
    if r.status_code == 200:
        data = json['data']
        print('Data retrieved from frost.met.no!')
    else:
        print('Error! Returned status code %s' % r.status_code)
        print('Message: %s' % json['error']['message'])
        print('Reason: %s' % json['error']['reason'])
        return None

    df = pd.DataFrame(columns=["id", "name", "geometry"])

    for row in data:
        df.loc[len(df)] = [row['id'], row['name'], row["geometry"]]

    lat = lambda x: re.findall(r'(\d+\.\d+)', str(x))[0]
    lon = lambda x: re.findall(r'(\d+\.\d+)', str(x))[1]

    df['lat'] = df['geometry'].apply(lat)
    df['lon']= df['geometry'].apply(lon)

    return df[['id', 'name', 'lat', 'lon']]

print(get_weather_station_latlon())