from typing import Any, Union

import pandas as pd
from py2neo.data import Node, Relationship
from py2neo import Graph
graph: Union[Graph, Any] = Graph("http://localhost:7474/browser/")
#df.groupby("(no genres listed)").sum()
#df.groupby("Documentary").sum()

df = pd.read_json("C:\\Users\\azz93\\Desktop\\movie_Azz\\movies_rated_tagged.json")
df.drop(df.columns[[0,1,12,26,24,28,27,30]], axis=1, inplace=True)
df.replace({'title': r'[(\d$)]'}, {'title': ' '}, regex=True, inplace=True)

genres = ("Documentary", "year", "IMAX", "Musical", "Animation", "Action", "Children", "Adventure", "Western",
          "(no genres listed)", "Thriller", "War", "Crime", "Horror", "Drama", "Film-Noir", "Romance", "Sci-Fi",
          "Comedy", "Fantasy", "Mystery")

df = df.drop_duplicates()
print(df)

for x in df["title"]:
    x = Node("Title", name=x)
    for y in genres:
        if df[y].iloc[count] == 1:
            y = Node("Genres", name=y)
            xy = Relationship(x, "Relations", y)
            graph.create(xy)
        count = count + 1
    print(Node)




