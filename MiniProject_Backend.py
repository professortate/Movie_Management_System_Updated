import sqlite3

def AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()

    cur.execute("INSERT OR IGNORE INTO Movies (Movie_ID, Movie_Name, Release_Date) VALUES (?, ?, ?)",
                (Movie_ID, Movie_Name, Release_Date))

    cur.execute("INSERT OR IGNORE INTO Directors (Director_Name) VALUES (?)", (Director,))
    cur.execute("SELECT id FROM Directors WHERE Director_Name=?", (Director,))
    Director_ID = cur.fetchone()[0]

    cur.execute("INSERT INTO MovieDetails (Movie_ID, Director_ID, Budget, Duration, Rating) VALUES (?, ?, ?, ?, ?)",
                (Movie_ID, Director_ID, Budget, Duration, Rating))

    for actor in Cast.split(','):
        cur.execute("INSERT OR IGNORE INTO Casts (Cast_Name) VALUES (?)", (actor.strip(),))
        cur.execute("SELECT id FROM Casts WHERE Cast_Name=?", (actor.strip(),))
        Cast_ID = cur.fetchone()[0]
        cur.execute("INSERT INTO MovieCasts (Movie_ID, Cast_ID) VALUES (?, ?)", (Movie_ID, Cast_ID))

    conn.commit()
    conn.close()

def ViewMovieData():
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT m.Movie_ID, m.Movie_Name, m.Release_Date, d.Director_Name, 
               GROUP_CONCAT(c.Cast_Name, ', ') AS Casts, md.Budget, md.Duration, md.Rating
        FROM Movies m
        LEFT JOIN MovieDetails md ON m.Movie_ID = md.Movie_ID
        LEFT JOIN Directors d ON md.Director_ID = d.id
        LEFT JOIN MovieCasts mc ON m.Movie_ID = mc.Movie_ID
        LEFT JOIN Casts c ON mc.Cast_ID = c.id
        GROUP BY m.Movie_ID
    """)

    rows = cur.fetchall()
    conn.close()
    return rows

def DeleteMovieRec(Movie_ID):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM Movies WHERE Movie_ID=?", (Movie_ID,))
    cur.execute("DELETE FROM MovieDetails WHERE Movie_ID=?", (Movie_ID,))
    cur.execute("DELETE FROM MovieCasts WHERE Movie_ID=?", (Movie_ID,))

    conn.commit()
    conn.close()

def SearchMovieData(Movie_ID="", Movie_Name=""):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()

    print(f"Searching for Movie_ID: {Movie_ID}, Movie_Name: {Movie_Name}")

    query = """
        SELECT m.Movie_ID, m.Movie_Name, m.Release_Date, d.Director_Name, 
               GROUP_CONCAT(c.Cast_Name, ', ') AS Casts, md.Budget, md.Duration, md.Rating
        FROM Movies m
        LEFT JOIN MovieDetails md ON m.Movie_ID = md.Movie_ID
        LEFT JOIN Directors d ON md.Director_ID = d.id
        LEFT JOIN MovieCasts mc ON m.Movie_ID = mc.Movie_ID
        LEFT JOIN Casts c ON mc.Cast_ID = c.id
        WHERE m.Movie_ID LIKE ? OR m.Movie_Name LIKE ?
        GROUP BY m.Movie_ID
    """

    cur.execute(query, ('%' + Movie_ID + '%', '%' + Movie_Name + '%'))

    rows = cur.fetchall()
    print(f"Search results: {rows}")
    conn.close()
    return rows

def UpdateMovieData(id, Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()

    cur.execute("UPDATE Movies SET Movie_Name=?, Release_Date=? WHERE Movie_ID=?", 
                (Movie_Name, Release_Date, Movie_ID))

    cur.execute("INSERT OR IGNORE INTO Directors (Director_Name) VALUES (?)", (Director,))
    cur.execute("SELECT id FROM Directors WHERE Director_Name=?", (Director,))
    Director_ID = cur.fetchone()[0]

    cur.execute("UPDATE MovieDetails SET Director_ID=?, Budget=?, Duration=?, Rating=? WHERE Movie_ID=?", 
                (Director_ID, Budget, Duration, Rating, Movie_ID))

    cur.execute("DELETE FROM MovieCasts WHERE Movie_ID=?", (Movie_ID,))
    for actor in Cast.split(','):
        cur.execute("INSERT OR IGNORE INTO Casts (Cast_Name) VALUES (?)", (actor.strip(),))
        cur.execute("SELECT id FROM Casts WHERE Cast_Name=?", (actor.strip(),))
        Cast_ID = cur.fetchone()[0]
        cur.execute("INSERT INTO MovieCasts (Movie_ID, Cast_ID) VALUES (?, ?)", (Movie_ID, Cast_ID))

    conn.commit()
    conn.close()
