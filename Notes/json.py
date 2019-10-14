import json
from pathlib import Path
movies = [ 
    {"id" : 1, "title" : "Terminator","year": 1984 }
    {"id" : 2, "title" : "kindergarten Cop", "year" : 1990}
]

data =  json.dumps(movies)
print(data)
Path("movies.json").write_text(data) 

dataRead = Path("movies.json").read_text()
moviesData = json.loads(dataRead)
print(moviesData[0]["title"])
