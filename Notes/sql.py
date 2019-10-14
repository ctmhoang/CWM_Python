import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
print(movies)
with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?,?,?)"
    for movie in movies:
        conn.execute(command, tuple(movie.value()))
    conn.commit()
    
#with sqlite3.connect("db.sqlite3") as conn:
    #comamnd = "SELECT * FROM Movies"
    #cusor = conn.execute(comamnd)
    ##for row in cursor:
        ##print(row)
    #movies = cursor.fetchall() #get a list
    #print(movies)
