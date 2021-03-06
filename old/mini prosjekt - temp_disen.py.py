
# Libraries needed (pandas is not standard and must be installed in Python)
import requests
import pandas as pd

# Insert your own client ID here
client_id = '5a54d482-9940-4128-8cac-fabf3a12344b'

# Define endpoint and parameters
endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources': 'SN18420,', #Disen. Blinderen har sourcekode SN18700
    'elements': 'air_temperature,',
    'referencetime': '2019-04-01/2019-04-03',
}
# Issue an HTTP GET request
r = requests.get(endpoint, parameters, auth=(client_id,''))
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

print(df)
