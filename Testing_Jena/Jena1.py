from rdflib import Graph, Namespace, RDF

# Load the ontology
g = Graph()
g.parse('data/moviesV4.rdf')  

# Define the namespace of your ontology
n = Namespace("http://www.semanticweb.org/dataset/ontologies/2024/4/moviesV1#")  

# Display all the Actors and Directors (which are subclasses of Person)
for s, p, o in g.triples((None, RDF.type, n.Actor)):
    print(s)
for s, p, o in g.triples((None, RDF.type, n.Director)):
    print(s)
for s, p, o in g.triples((None, RDF.type, n.Writer)):
    print(s)

