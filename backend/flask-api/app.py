import sqlite3
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('sql/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    
    conn.close()
    return "done"

@app.route('/players')
def players():
    conn = get_db_connection()
    players = conn.execute('SELECT id, player_name, team, position FROM players').fetchall()
    players_array = []
    for p in players:
        players_array.append({
            'id': p[0],
            'name': p[1],
            'position': p[3],
            'team': p[2],
        })
    return jsonify(players_array)
    # return "players route"
