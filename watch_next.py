import spacy

# Load the English language model
nlp = spacy.load('en_core_web_md')

# Read in the movies.txt file and create a list of documents
with open('movies.txt', 'r') as f:
    movies = [nlp(line.strip()) for line in f]

# Define a function to find the most similar movie
def find_similar_movie(description):
    # Convert the description to a spaCy document
    doc = nlp(description)
    # Calculate the similarity between the description and each movie
    similarities = [doc.similarity(movie) for movie in movies]
    # Get the index of the most similar movie
    index = similarities.index(max(similarities))
    # Return the title of the most similar movie using Unicode code and idx is the index
    return f"Movie {chr(ord('A') + index)}"

# Test the function with the provided description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(find_similar_movie(description))
