import sqlite3
import requests
import fnmatch

def make_players_table():
    # Make API call to MFL to get players
    r = requests.get("https://www43.myfantasyleague.com/2023/export?TYPE=players&L=39638&APIKEY=&DETAILS=&SINCE=&PLAYERS=&JSON=1")
    players = r.json()['players']['player'] # list of players at this point

    # Process out non offensive players
    nonOffensivePositions = ['CB', 'S', 'LB', 'DE', 'DL', 'DT', 'PN', 'PK', 'Coach', 'Off', 'Def', 'ST']
    processedPlayers = [x for x in players if not fnmatch.fnmatch(x['position'], 'TM*') and 
                            x['position'] not in nonOffensivePositions
                        ]

    for p in processedPlayers:
        data_tuple = (p['id'], p['name'], p['team'], p['position'])
        cur.execute("INSERT INTO players (id, player_name, team, position) VALUES (?, ?, ?, ?)", data_tuple)

def make_rosters_table():
    # Make API call to MFL to get players
    r = requests.get("https://www43.myfantasyleague.com/2023/export?TYPE=rosters&L=39638&APIKEY=&FRANCHISE=&W=&JSON=1")

    # Process information 
    rosters = r.json()['rosters']['franchise'] # list of 10 rosters
    for r in rosters:
        id = r['id']
        for p in r['player']:
            data_tuple = (id, p['id'], p['salary'], p['contractStatus'], p['contractYear'], p['contractInfo'])
            cur.execute("INSERT INTO rosters (franchise_id, player_id, salary, contract_status, contract_year, contract_info) VALUES (?, ?, ?, ?, ?, ?)", data_tuple)

def make_franchise_table():
    # Make API call to MFL to get players
    r = requests.get("https://www43.myfantasyleague.com/2023/export?TYPE=league&L=39638&APIKEY=&JSON=1")

    # Process information 
    franchises = r.json()['league']['franchises']['franchise']
    for f in franchises:
        sca = f['salaryCapAmount']
        if sca == '':
            sca = 1000
        total_salary = int(sca) - float(f['bbidAvailableBalance'])
        data_tuple = (f['id'], f['bbidAvailableBalance'], total_salary, f['division'], f['logo'], f['name'])
        cur.execute("INSERT INTO franchises (franchise_id, cap_space, total_salary, division, logo, franchise_name) VALUES (?, ?, ?, ?, ?, ?)", data_tuple)

connection = sqlite3.connect('sql/database.db')

with open('sql/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Players table
make_players_table()

# Rosters table
make_rosters_table()

# Franchises table
make_franchise_table()


connection.commit()
connection.close()