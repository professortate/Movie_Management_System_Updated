import sqlite3

def MovieData():
    conn = sqlite3.connect("movieDatabase.db")
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Movies (
            id INTEGER PRIMARY KEY,
            Movie_ID TEXT UNIQUE,
            Movie_Name TEXT,
            Release_Date TEXT
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Directors (
            id INTEGER PRIMARY KEY,
            Director_Name TEXT UNIQUE
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Casts (
            id INTEGER PRIMARY KEY,
            Cast_Name TEXT UNIQUE
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS MovieDetails (
            id INTEGER PRIMARY KEY,
            Movie_ID TEXT,
            Director_ID INTEGER,
            Budget TEXT,
            Duration TEXT,
            Rating TEXT,
            FOREIGN KEY (Movie_ID) REFERENCES Movies (Movie_ID),
            FOREIGN KEY (Director_ID) REFERENCES Directors (id)
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS MovieCasts (
            id INTEGER PRIMARY KEY,
            Movie_ID TEXT,
            Cast_ID INTEGER,
            FOREIGN KEY (Movie_ID) REFERENCES Movies (Movie_ID),
            FOREIGN KEY (Cast_ID) REFERENCES Casts (id)
        )
    """)
    
    conn.commit()
    conn.close()

MovieData()
