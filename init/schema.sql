CREATE TABLE IF NOT EXISTS candidates(
    id TEXT PRIMARY KEY,
    name TEXT,
    vote_qnt INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS computerIP(
    ip TEXT PRIMARY KEY,
    voted BOOLEAN DEFAULT False
);