# Movies_Ontology

This project models an ontology of movies. Protégé Editor was used to create this ontology of movies. Basically, we aim to create a blueprint 
for the online referencing and storage of movie datasets. This ontology will be used to model a python desktop application to reason querying 
and selecting movies according to the required included and excluded individuals. This work is divided into sections corresponding to the 
given project description. Part I models the ontology, Part II populates the ontology and checks for consistency, Part III performs SPARQL 
queries, Part IV uses Jena and rdflib to test SPARQL queries and finally, Part V focuses on a user-friendly interface to query the ontology.

## Overview and Description of Ontology

![image](https://github.com/PerfectionistAF/Movies_Ontology/assets/77901496/5fda46d8-0092-40c0-a623-29927487d4eb)

**1) Class:** 

a) Movie: defines basic Movie class<br>
b) Genre: defines basic Genre class<br> 
c) Person: defines basic Person class<br>
d) Actor: basic Actor class is a subclass of Person class<br>
e) Writer: basic Writer class is a subclass of Person<br>
f) Director: basic Director class is a subclass of Person<br>

**2) Object Property:**

a) hasGenre: Each Movie has one or more instances of class Genre<br>
b) hasActor: Each Movie has at least one instance of class Actor<br>
c) hasWriter: Each Movie has at least one instance of class Writer<br>
d) hasDirector: Each Movie has at least one instance of class Director<br>
e) isGenreOf: Inverse of hasGenre<br>
f) isActorOf: Inverse of hasActor<br>
g) isDirectorOf: Inverse of hasDirector<br>
h) isWriterOf: Inverse of hasWriter<br>

**3) Data Property:**

a) name: Name of Person<br>
b) age: Age of Person<br>
c) nationality: Nationality(s) of Person<br>
d) gender: Gender of Person<br>
e) genre: Genre(s) of Movie<br>
f) title: Title of Movie<br>
g) country: Country(s) of Production of Movie<br>
h) language: Language(s) of Movie<br>
i) year: Year of Copyright of Movie<br>

## Person Instances on OntoGraf

![image](https://github.com/PerfectionistAF/Movies_Ontology/assets/77901496/f43cada2-bdf0-4766-a2b3-8f6c9217b9b1)

### a) Actors

![image](https://github.com/PerfectionistAF/Movies_Ontology/assets/77901496/d56f66db-90da-4d75-9264-bb5af8920ef4)

### b) Directors

![image](https://github.com/PerfectionistAF/Movies_Ontology/assets/77901496/835b19ca-b752-4b42-a137-f6c9c51db2a9)

### c) Writers

![image](https://github.com/PerfectionistAF/Movies_Ontology/assets/77901496/df454305-8bbe-49cd-b9ca-65a572be7a40)

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:
```bash
pip install tkinter
pip install rdflib
```
### Node.js

Use the npm [npm](https://docs.npmjs.com/cli/v10/commands/npm-install) to install the following:
```bash
npm install -g @comunica/query-sparql
```

```bash
comunica-sparql-http http://www.semanticweb.org/dataset/ontologies/2024/4/moviesV1/
```

By default, the endpoint at http://localhost:3000/sparql 

## Main Interface

![image](https://github.com/PerfectionistAF/Movies_Ontology/assets/77901496/dec9bb4e-f7bf-4ea8-812f-2b963797a00e)

## Installation and Running

Install the code from : [https://github.com/PerfectionistAF/Movies_Ontology/src/main ](https://github.com/PerfectionistAF/Movies_Ontology/tree/main/src/main/movies_home)
```bash
python header.py
python engine.py
python movies_home.py
```

***header.py***: global SPARQL query pattern<br>
***engine.py***: global SPARQL finding function<br>
***movies_home.py***: generate main interface and results<br>

## Testing

![image](https://github.com/PerfectionistAF/Movies_Ontology/assets/77901496/35965b84-00c5-4381-823f-dd115448b9e8)

