import sqlite3

def get_db_connection():
    conn = sqlite3.connect('sql/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_data():
    conn = get_db_connection()
    players = conn.execute('SELECT * FROM players').fetchall()
    rosters = conn.execute('SELECT * FROM rosters').fetchall()
    franchises = conn.execute('SELECT * FROM franchises').fetchall()
    # for f in franchises:
    #     for shit in f:
    #         print(shit)
    for post in rosters:
        for shit in post:
            print(shit)
    conn.close()
    return "Butt"

if __name__ == "__main__":
    get_data()