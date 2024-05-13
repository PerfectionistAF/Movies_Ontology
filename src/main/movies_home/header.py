# Define the SPARQL query pattern globally
pattern = """
PREFIX ont: <http://www.semanticweb.org/dataset/ontologies/2024/4/moviesV1#>
SELECT DISTINCT ?movieTitle
WHERE {{
    ?movie rdf:type ont:Movie .
    {actor_patterns}
    {director_patterns}
    {genre_patterns}
    ?movie ont:title ?movieTitle .
}}
"""
