import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()

tmdb.api_key = '8bb4b82b6e1ba737ba1160f1a26dedef'


def get_recommendations(title):
    # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index값을 얻음
    idx = movies[movies['title'] == title].index[0]

    # 코사인 유사도 매트릭스 (cosine_sim)에서 idx 에 해당하는 데이터를 (idx, 유사도)
    # 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]

    # 추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]

    # 인덱스 정보를 통해 영화 제목 추출
    images = []
    titles = []

    for i in movie_indices:
        id = movies['id'].iloc[i]
        details = movie.details(id)

        images.append('https://image.tmdb.org/t/p/w500' +
                      details['poster_path'])
        titles.append(details['title'])


movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

st.set_page_config(layout='wide')
st.header('Yeonuelflix')


movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like the most', movie_list)

if st.button('Recommend'):
    images, titles = get_recommendations(title)
