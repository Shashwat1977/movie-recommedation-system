import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
     response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=cffbd393c777f3fcf561df2eb360651d&language=en-US')
     data = response.json()
     return "https://image.tmdb.org/t/p/w500"+data['poster_path']
st.title('Movie Recommedation system')
string_key = "cffbd393c777f3fcf561df2eb360651d"
movie_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movie_list)
similarity = pickle.load(open('similarity.pkl','rb'))
option = st.selectbox(
     'How would you like to be contacted?',
     (movies['title'].values))


def recommend(movie):
     index = movies[movies['title'] == movie]['movie_id'].index[0]
     distances = similarity[index]
     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
     rm = []
     rmposter = []
     for i in movie_list:
          movie_id = movies.iloc[i[0]].movie_id
          rm.append(movies.iloc[i[0]].title)
          rmposter.append(fetch_poster(movie_id))
     return rm,rmposter
if st.button('Recommend'):
     names,posters = recommend(option)
     col1, col2, col3,col4,col5 = st.columns(5)
     with col1:
          st.write(names[0])
          st.image(posters[0])

     with col2:
          st.write(names[1])
          st.image(posters[1])

     with col3:
          st.write(names[2])
          st.image(posters[2])

     with col4:
          st.write(names[3])
          st.image(posters[3])

     with col5:
          st.write(names[4])
          st.image(posters[4])