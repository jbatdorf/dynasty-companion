const express = require('express')
const sqlite3 = require('sqlite3').verbose()
const app = express()
const port = 3000

const DBSOURCE = '../flask-api/sql/database.db'
const getAllPlayersSql = 'SELECT id, player_name, team, position FROM players'

let db = new sqlite3.Database(DBSOURCE, (err) => {
    if (err) {
      // Cannot open database
      console.error(err.message)
      throw err
    }else{
        console.log('Connected to the SQLite database.')
    }

})

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/players', (req, res) => {
    let players = []
    db.all(getAllPlayersSql, (err, rows) => {
        if(err) {
            throw err;
        }

        rows.forEach((row) => {
            players.push(row);
        });

        res.send(players)
    })    
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})