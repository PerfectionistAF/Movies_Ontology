from rdflib import Graph, Namespace, RDF, RDFS, BNode, Literal

# Load the ontology
g = Graph()
g.parse('data/moviesV4.rdf')  
# Define the namespace of your ontology
n = Namespace("http://www.semanticweb.org/dataset/ontologies/2024/4/moviesV1#")  

# Create a new class ActorDirector
ActorDirector = n["ActorDirector"]
g.add((ActorDirector, RDF.type, RDFS.Class))
g.add((ActorDirector, RDFS.label, Literal("ActorDirector")))

# Find all persons that are both actors and directors, and add them to the ActorDirector class
for s in g.subjects(RDF.type, n.Actor):
    if (s, RDF.type, n.Director) in g:
        g.add((s, RDF.type, ActorDirector))

# Display all ActorDirectors
for s in g.subjects(RDF.type, ActorDirector):
    print(s)
