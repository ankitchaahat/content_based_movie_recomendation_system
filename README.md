# content_based_movie_recomendation_system



This project is about building a content-based movie recommendation system using the "TMDB 5000 Movies" and "TMDB 5000 Credits" datasets.
The goal is to recommend movies that are similar to a given movie based on the content, such as genres, keywords, cast, and crew.




# 1. Data Loading:

Load the datasets tmdb_5000_movies.csv and tmdb_5000_credits.csv into Pandas DataFrames named movies and credits.


# 2. Data Exploration:

Display the first row of each dataset to explore the columns using movies.head(1) and credits.head(1)['crew'].


# 3. Data Merging:

Merge the two datasets on the title column using movies.merge(credits, on='title') to create a single DataFrame that contains all relevant information about each movie.


# 4. Selecting Relevant Columns:

Keep only the columns that are necessary for the recommendation system: movie_id, title, overview, genres, keywords, cast, and crew.


# 5. Handling Missing Values:

Check for missing values in the dataset using movies.isnull().sum() and drop any rows with missing values using movies.dropna(inplace=True).


# 6. Handling Duplicate Values:

Check for duplicate entries using movies.duplicated().sum().


# 7. Processing 'genres' and 'keywords' Columns:

Convert the JSON-like strings in the 'genres' and 'keywords' columns into Python lists using the ast module. The function convert extracts the 'name' field from each dictionary in the list.


# 8. Processing 'cast' Column:

Extract the top 3 cast members from the 'cast' column using the function convert3.


# 9. Processing 'crew' Column:

Extract the director's name from the 'crew' column using the function fetch_director.


# 10. Processing 'overview' Column:

Convert the movie overview text into a list of words using a lambda function: movies['overview'].apply(lambda x: x.split()).


# 11. Removing Spaces from Words:

Remove spaces between words in the 'genres', 'keywords', 'cast', and 'crew' columns to create single words without spaces using a lambda function: lambda x: [i.replace(" ", "") for i in x].


# 12. Creating 'tags' Column:

Combine the processed 'overview', 'genres', 'keywords', 'cast', and 'crew' columns into a single 'tags' column to represent the movie content as a single text entity.


# 13. Creating a New DataFrame:

Create a new DataFrame new_df that contains only the 'movie_id', 'title', and 'tags' columns for further processing.


# 14. Converting Tags to Lowercase:

Convert all text in the 'tags' column to lowercase to ensure uniformity in text processing.


# 15. Text Preprocessing with Stemming:

Apply stemming to the 'tags' column using the Porter Stemmer from NLTK to reduce words to their root form, enhancing the similarity matching process.


# 16. Vectorization of Text Data:

Convert the 'tags' column into numerical vectors using CountVectorizer from sklearn with a maximum of 5000 features and removal of English stop words. This transforms the text data into a format that can be used for computing similarities.


# 17. Computing Cosine Similarity:

Compute cosine similarity between the vectors using cosine_similarity to find how similar each movie is to all other movies.


# 18. Defining a Recommendation Function:

Define a function recommend(movie) that:

Finds the index of the input movie.

Retrieves the similarity scores for the input movie against all others.

Sorts the list of movies based on similarity scores in descending order (excluding the input movie itself).

Prints the top 5 most similar movies.


# 19. Saving Models Using Pickle:

Save the new_df DataFrame and the similarity matrix using the pickle library to store the processed data and computed similarities for later use.

********************************************************************************************************************************************************
# Purpose and Outcome:

The project processes movie data to create a content-based recommendation system. The main idea is to recommend movies that are similar in content (based on genres, keywords, cast, and crew) to a given movie using cosine similarity. The outcome is a system where, given the title of a movie, the recommend() function returns the top 5 similar movies.






