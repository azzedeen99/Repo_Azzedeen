
df.drop(df.columns[[0,1,12,26,24,28,27,30]], axis=1, inplace=True)

with open('movies_rated_tagged.json', 'r') as myfile:
    data = myfile.read()
#print (data)
from py2neo import Graph , Relationship, Node
graph = Graph()
remote_graph = Graph("http://localhost:7474/%22)")

Titre = Node(name="Title")
Genre = Node(name="Genres")
ab = Relationship(Titre, "KNOWS", Genre)
graph.create(ab)