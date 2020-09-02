client_id = os.environ['FROST_API_CLIENT_ID']

endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources': 'SN18420,', #disen
    'elements': 'air_temperature,',
    'referencetime': '2020-01-01/2020-09-01',
}
r = requests.get(endpoint, parameters, auth=(client_id,''))

json = r.json()


data = json['data']


import psycopg2

conn = psycopg2.connect(host = "ds-etl-academy.cgbivchwjzle.eu-west-1.rds.amazonaws.com",
                       dbname = "team_ccm",
                       user = "student_martin",
                       password = "kake",
                       port = 5432
                       )
cur = conn.cursor()

for row in data:
    query = '''insert into temperatur(temp_grader, vær_stasjon_id, 
                temp_date_time) VALUES (%s, %s, %s);'''
    
    param = [str(row['observations'][0]['value']), 
             str(row['sourceId']), 
             str(row['referenceTime'])]
    
    print(query)
    cur.execute(query, param)


conn.commit()

cur.close()


# conn.close()
