import streamlit as st
import pickle
import pandas as pd
import requests


st.set_page_config(layout="wide")

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)






def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ea5a526d12e1d0d581e9680c4ca69a55'.format((movie_id)))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    # Sorting the distances and also keeping the indices

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.markdown("<h1 style='text-align: center; color: White;'>Movie Recommendation System</h1>", unsafe_allow_html=True)

selected_movie_name = st.selectbox('Select a movie of your choice',movies['title'].values)
if st.button('Recommend Movies'):
    names,posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:

        new_title = '<p style="font-family:sans-serif; color:White; font-size: 20px;">'+names[0]+'</p>'
        remarks = '<p style="font-family:sans-serif; color:#69B620; font-size: 15x;">(Most Match)</p>'
        st.markdown(remarks, unsafe_allow_html=True)
        st.markdown(new_title, unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        new_title = '<p style="font-family:sans-serif; color:White; font-size: 20px;">' + names[1] + '</p>'
        remarks = '<p style="font-family:sans-serif; color:#A3CA22; font-size: 15x;">(2nd Match)</p>'
        st.markdown(remarks, unsafe_allow_html=True)
        st.markdown(new_title, unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        new_title = '<p style="font-family:sans-serif; color:White; font-size: 20px;">' + names[2] + '</p>'
        remarks = '<p style="font-family:sans-serif; color:#BFCA22; font-size: 15x;">(3rd Match)</p>'
        st.markdown(remarks, unsafe_allow_html=True)
        st.markdown(new_title, unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        new_title = '<p style="font-family:sans-serif; color:White; font-size: 20px;">' + names[3] + '</p>'
        remarks = '<p style="font-family:sans-serif; color:Yellow; font-size: 15x;">(4th Match)</p>'
        st.markdown(remarks, unsafe_allow_html=True)
        st.markdown(new_title, unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        new_title = '<p style="font-family:sans-serif; color:White; font-size: 20px;">' + names[4] + '</p>'
        remarks = '<p style="font-family:sans-serif; color:Orange; font-size: 15x;">(5th Match)</p>'
        st.markdown(remarks, unsafe_allow_html=True)
        st.markdown(new_title, unsafe_allow_html=True)
        st.image(posters[4])