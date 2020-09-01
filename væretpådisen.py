
# Libraries needed (pandas is not standard and must be installed in Python)
import requests
import pandas as pd
import os

# Insert your own client ID here
CLIENT_ID = os.environ['FROST_API_CLIENT_ID']

def get_weather_on_station(sourceId):
    """Get the weather on a particular station for the month of April

    Args:
        sourceId (str): sourceId for a weather station in FrostAPI

    Returns:
        Pandas Dataframe: columns = sourceID, referenceTime, elementId, value, unit
    """    
    endpoint = 'https://frost.met.no/observations/v0.jsonld'
    parameters = {
        'sources': f'{sourceId},', #disen
        'elements': 'air_temperature,',
        'referencetime': '2019-04-01/2019-05-01',
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
        # This will return a Dataframe with all of the observations in a table format
    df = pd.DataFrame()
    for i in range(len(data)):
        row = pd.DataFrame(data[i]['observations'])
        row['referenceTime'] = data[i]['referenceTime']
        row['sourceId'] = data[i]['sourceId']
        df = df.append(row)
    df = df.reset_index()
    return df[['sourceId', 'referenceTime', 'elementId', 'value', 'unit']]

print(get_weather_on_station('SN18420'))
