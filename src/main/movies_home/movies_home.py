import tkinter as tk
from tkinter import messagebox
from rdflib import Graph
from tkinter import ttk

import header  ##to import global pattern variable
import engine  ##to import functions used to query 

# Function to handle search button click
def search_movies():
    included_actors = included_actors_entry.get().strip().split(",") if included_actors_entry.get().strip() else []
    excluded_actors = excluded_actors_entry.get().strip().split(",") if excluded_actors_entry.get().strip() else []
    included_directors = included_directors_entry.get().strip().split(",") if included_directors_entry.get().strip() else []
    excluded_directors = excluded_directors_entry.get().strip().split(",") if excluded_directors_entry.get().strip() else []
    included_genres = included_genres_entry.get().strip().split(",") if included_genres_entry.get().strip() else []
    excluded_genres = excluded_genres_entry.get().strip().split(",") if excluded_genres_entry.get().strip() else []

    # Check if any criterion is provided
    if not any([included_actors, excluded_actors, included_directors, excluded_directors, included_genres, excluded_genres]):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter at least one criterion to perform the search.")
        return

    movies = engine.get_movies(included_actors=included_actors, excluded_actors=excluded_actors,
                        included_directors=included_directors, excluded_directors=excluded_directors,
                        included_genres=included_genres, excluded_genres=excluded_genres)

    result_text.delete(1.0, tk.END)
    if movies:
        result_text.insert(tk.END, "\n".join(movies))
    else:
        result_text.insert(tk.END, "No movies found matching the specified criteria.")



# Create main window
root = tk.Tk()
root.geometry("420x420")
root.title("Movie Search")

# Create labels and entry fields for user input
included_actors_label = ttk.Label(root, text="Included Actors (csv):")
included_actors_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
included_actors_entry = ttk.Entry(root)
included_actors_entry.grid(row=0, column=1, padx=5, pady=5)

excluded_actors_label = ttk.Label(root, text="Excluded Actors (csv):")
excluded_actors_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
excluded_actors_entry = ttk.Entry(root)
excluded_actors_entry.grid(row=1, column=1, padx=5, pady=5)

included_directors_label = ttk.Label(root, text="Included Directors (csv):")
included_directors_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
included_directors_entry = ttk.Entry(root)
included_directors_entry.grid(row=2, column=1, padx=5, pady=5)

excluded_directors_label = ttk.Label(root, text="Excluded Directors (csv):")
excluded_directors_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
excluded_directors_entry = ttk.Entry(root)
excluded_directors_entry.grid(row=3, column=1, padx=5, pady=5)

included_genres_label = ttk.Label(root, text="Included Genres (csv):")
included_genres_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
included_genres_entry = ttk.Entry(root)
included_genres_entry.grid(row=4, column=1, padx=5, pady=5)

excluded_genres_label = ttk.Label(root, text="Excluded Genres (csv):")
excluded_genres_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
excluded_genres_entry = ttk.Entry(root)
excluded_genres_entry.grid(row=5, column=1, padx=5, pady=5)


# Create a button to trigger the search
search_button = ttk.Button(root, text="Search", command=search_movies)
search_button.grid(row=6, column=1, columnspan=1, padx=5, pady=5)

# Create a text widget to display the results
result_text = tk.Text(root, width=50, height=10)
result_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
