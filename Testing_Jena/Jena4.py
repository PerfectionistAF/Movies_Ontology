from rdflib import Graph, Namespace, RDF, Literal
from rdflib.plugins.sparql import prepareQuery

# Load the ontology
g = Graph()
g.parse('data/moviesV4.rdf') 

# Define the namespace of your ontology
n = Namespace("http://www.semanticweb.org/dataset/ontologies/2024/4/moviesV1#")  

# Read a name of a movie
movie_name = input("Enter the name of a movie: ")

# Check if the movie exists in the ontology
movie = n[movie_name]
if (movie, RDF.type, n.Movie) not in g:
    print("Error: The movie does not exist.")
else:
    # Display the movie's details
    query_text = """
        SELECT ?year ?country ?genre ?actor WHERE {
            ns:%s ns:year ?year .
            ns:%s ns:country ?country .
            ns:%s ns:hasGenre ?genre .
            ns:%s ns:hasActor ?actor .
        }
    """ % (movie_name, movie_name, movie_name, movie_name)
    query = prepareQuery(query_text, initNs={"ns": n})
    for row in g.query(query):
        print(f"Year: {row[0]}, Country: {row[1]}, Genre: {row[2]}, Actor: {row[3]}")
