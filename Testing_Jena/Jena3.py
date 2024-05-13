from rdflib import Graph, Namespace, RDF
import owlrl

# Load the ontology
g = Graph()
g.parse('data/moviesV4.rdf')  
# Perform OWL reasoning
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)

# Define the namespace of your ontology
n = Namespace("http://www.semanticweb.org/dataset/ontologies/2024/4/moviesV1#")

# Display all the Actors
for s, p, o in g.triples((None, RDF.type, n.Actor)):
    print(s)
