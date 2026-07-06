import pickle
import streamlit as st
import requests
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies








# Streamlit UI

st.header("Movie Recommender System")


movies = pickle.load(open("moviesdict.pkl", "rb"))
movies=pd.DataFrame(movies)
similarity = pickle.load(open("similarity.pkl", "rb"))



movie_list = movies['title'].values


selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button("Recommend"):
    names = recommend(selected_movie)

    for name in names:
        st.write(name)

