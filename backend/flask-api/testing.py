import sqlite3
import requests
import json
import fnmatch

# Make API call to MFL to get players
r = requests.get("https://www43.myfantasyleague.com/2023/export?TYPE=league&L=39638&APIKEY=&JSON=1")

# Process information 
franchises = r.json()['league']['franchises']['franchise']
for f in franchises:
    sca = f['salaryCapAmount']
    if sca is '':
        sca = 1000
    total_salary = int(sca) - float(f['bbidAvailableBalance'])
    data_tuple = (f['id'], f['bbidAvailableBalance'], total_salary, f['division'], f['logo'], f['name'])


# Push rows into database

