import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()

tmdb.api_key = '8bb4b82b6e1ba737ba1160f1a26dedef'

movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

st.set_page_config(layout='wide')
st.header('Yeonuelflix')


movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like the most', movie_list)

if st.button('Recommend'):
    images, titles = get_recommendations(title),
