from rdflib import Graph, Namespace, RDF, RDFS, BNode, Literal

# Load the ontology
g = Graph()
g.parse('data/moviesV4.rdf') 

# Define the namespace of your ontology
n = Namespace("http://www.semanticweb.org/dataset/ontologies/2024/4/moviesV1#")  

# Rule 1: If a person is an actor and a director, then they are an ActorDirector
ActorDirector = n["ActorDirector"]
g.add((ActorDirector, RDF.type, RDFS.Class))
g.add((ActorDirector, RDFS.label, Literal("ActorDirector")))
for s in g.subjects(RDF.type, n.Actor):
    if (s, RDF.type, n.Director) in g:
        g.add((s, RDF.type, ActorDirector))

# Rule 2: If a movie has a genre Thriller, then it is a ThrillerMovie
ThrillerMovie = n["ThrillerMovie"]
g.add((ThrillerMovie, RDF.type, RDFS.Class))
g.add((ThrillerMovie, RDFS.label, Literal("ThrillerMovie")))
for s in g.subjects(n.hasGenre, n.Thriller):
    g.add((s, RDF.type, ThrillerMovie))

# Rule 3: If a movie was released after the year 2000, then it is a ModernMovie
ModernMovie = n["ModernMovie"]
g.add((ModernMovie, RDF.type, RDFS.Class))
g.add((ModernMovie, RDFS.label, Literal("ModernMovie")))
for s, o in g.subject_objects(n.year):
    if int(o) > 2000:
        g.add((s, RDF.type, ModernMovie))

# Display all ActorDirectors, ThrillerMovies, and ModernMovies
print("ActorDirectors:")
for s in g.subjects(RDF.type, ActorDirector):
    print(s)
print("\nThrillerMovies:")
for s in g.subjects(RDF.type, ThrillerMovie):
    print(s)
print("\nModernMovies:")
for s in g.subjects(RDF.type, ModernMovie):
    print(s)
