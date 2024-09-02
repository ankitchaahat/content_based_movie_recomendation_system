import pandas as pd
import streamlit as st
import pickle

# Load the movies list DataFrame from the pickle file
movies_list = pickle.load(open('movies.pkl', 'rb'))

# Extract movie titles for the dropdown
movie_titles = movies_list['title'].values

# Load the similarity matrix from the pickle file
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    # Find the index of the selected movie
    movie_index = movies_list[movies_list['title'] == movie].index[0]

    # Get the pairwise similarity scores of all movies with the selected movie
    distances = similarity[movie_index]

    # Sort movies based on similarity scores (in descending order)
    movies_with_distances = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Get the movie titles for the top 5 recommendations
    recommended_movies = [movies_list.iloc[i[0]]['title'] for i in movies_with_distances]

    return recommended_movies


# Streamlit UI
st.title('Movie Recommender System')

# Dropdown to select a movie
selected_movie_name = st.selectbox('Select a movie', movie_titles)

# Button to trigger the recommendation
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)
