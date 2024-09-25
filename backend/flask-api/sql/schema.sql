DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS rosters;
DROP TABLE IF EXISTS franchises;

CREATE TABLE players (
    id INTEGER PRIMARY KEY,
    player_name TEXT NOT NULL,
    team TEXT NOT NULL,
    position TEXT NOT NULL
);

CREATE TABLE rosters (
    franchise_id INTEGER,
    player_id INTEGER PRIMARY KEY,
    salary INTEGER,
    contract_status TEXT,
    contract_year INTEGER,
    contract_info TEXT
);

CREATE TABLE franchises (
    franchise_id INTEGER PRIMARY KEY,
    cap_space INTEGER,
    total_salary INTEGER,
    division INTEGER NOT NULL,
    logo TEXT,
    franchise_name TEXT NOT NULL
);