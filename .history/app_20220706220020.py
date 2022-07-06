import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()

tmdb.api_key = '8bb4b82b6e1ba737ba1160f1a26dedef'
