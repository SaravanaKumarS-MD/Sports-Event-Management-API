import sqlite3

DB_NAME = "sports.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Sports Events Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            sport TEXT NOT NULL,
            venue TEXT NOT NULL,
            event_date TEXT NOT NULL,
            status TEXT DEFAULT 'Upcoming'
        )
    """)

    # Teams Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_name TEXT NOT NULL,
            captain TEXT NOT NULL,
            event_id INTEGER,
            FOREIGN KEY (event_id) REFERENCES events(id)
        )
    """)

    # Players Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            age INTEGER,
            team_id INTEGER,
            FOREIGN KEY (team_id) REFERENCES teams(id)
        )
    """)

    # Matches Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER,
            team1_id INTEGER,
            team2_id INTEGER,
            match_date TEXT,
            score1 INTEGER DEFAULT 0,
            score2 INTEGER DEFAULT 0,
            winner TEXT,
            status TEXT DEFAULT 'Scheduled',
            FOREIGN KEY (event_id) REFERENCES events(id),
            FOREIGN KEY (team1_id) REFERENCES teams(id),
            FOREIGN KEY (team2_id) REFERENCES teams(id)
        )
    """)

    conn.commit()
    conn.close()

    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_tables()