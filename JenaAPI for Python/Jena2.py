from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

# Load the ontology
g = Graph()
g.parse('data/moviesV4.rdf')  

# Define the namespace of your ontology
n = Namespace("http://www.semanticweb.org/dataset/ontologies/2024/4/moviesV1#")  

# Define the SPARQL query
query_text = """
    SELECT DISTINCT ?person WHERE {
        { ?person rdf:type ns:Actor . }
        UNION
        { ?person rdf:type ns:Director . }
        UNION
        { ?person rdf:type ns:Writer . }
    }
"""
#SELECT ?person WHERE {
#        { ?person rdf:type ns:Actor . }
#        UNION
#        { ?person rdf:type ns:Director . }
#    }
query = prepareQuery(query_text, initNs={"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "ns": n})

# Execute the query and print the results
for row in g.query(query):
    print(row[0])