## functions used to query inputs
#import movies_home  ##import to get your inputs into the function parameters correctly
from rdflib import Graph

import header       ##to import global pattern variable
# Function to get movies
def get_movies(included_actors=[], excluded_actors=[], included_directors=[], excluded_directors=[], included_genres=[], excluded_genres=[]):
    graph = Graph()
    rdf_file = "data/moviesV4_1.rdf"
    graph.parse(rdf_file, format="xml")

    actor_patterns = ""
    for actor in included_actors:
        actor_patterns += "?movie ont:hasActor ont:{} .\n".format(actor)
    for actor in excluded_actors:
        actor_patterns += "FILTER NOT EXISTS {{ ?movie ont:hasActor ont:{} }} .\n".format(actor)

    director_patterns = ""
    for director in included_directors:
        director_patterns += "?movie ont:hasDirector ont:{} .\n".format(director)
    for director in excluded_directors:
        director_patterns += "FILTER NOT EXISTS {{ ?movie ont:hasDirector ont:{} }} .\n".format(director)

    genre_patterns = ""
    for genre in included_genres:
        genre_patterns += "?movie ont:hasGenre ont:{} .\n".format(genre)
    for genre in excluded_genres:
        genre_patterns += "FILTER NOT EXISTS {{ ?movie ont:hasGenre ont:{} }} .\n".format(genre)

    query = header.pattern.format(actor_patterns=actor_patterns, director_patterns=director_patterns, genre_patterns=genre_patterns)

    results = graph.query(query)

    movies = [result.movieTitle for result in results]

    return movies

# Function to prompt user for values
def prompt_user_for_values(parameter_name):
    values = []
    while True:
        value = input("Enter a {parameter_name} (or leave blank to finish): ").strip(). format(parameter_name)
        if not value:
            break
        values.append(value.replace(" ", "_"))  # Replace spaces with underscores for consistency
    return values




