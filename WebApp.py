#-------------------------------------------DECLARARTIONS-------------------------------------------------------------------------------------
# # This Web app is made using streamlit
# The code can be run using ----> $streamlit run WebApp.py
# The app should be run after installing all dependencies
# This app is already deployed in Heroku and can be found here:https://movie-recommend-eng.herokuapp.com/
# The app takes a bit time to load for the first time but thereafter loads fast
# This project is made using jupyter notebook (for model development) and python (for app development)
# The front end is developed using streamlit
import streamlit as st
import pickle
import pandas as pd
import requests

#making the web page occupy the entire screen
st.set_page_config(layout="wide")

# Fetches the poster of the given movie from the TMDB website using API key
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ea5a526d12e1d0d581e9680c4ca69a55'.format((movie_id)))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


# returns recommended movie names and their respective posters on the basis of users movie selection
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

# getting a movies dictionary from the pickle file developed from the jupyter notebook file
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

#storing the similarity indices between the movies developed from the jupyter notebook file
similarity = pickle.load(open('similarity.pkl','rb'))

#setting the title of the website as "Movie Recommendation System"
st.markdown("<h1 style='text-align: center; color: White;'>Movie Recommendation System</h1>", unsafe_allow_html=True)

#Creating the dropdown menu for the list of movies and the "Recommend Movies" button
selected_movie_name = st.selectbox('Select a movie of your choice',movies['title'].values)
if st.button('Recommend Movies'):
    names,posters = recommend(selected_movie_name)


    # Creating 5 columns, one column for each movie and the most recommended movie to be 
    # found on column 1, the 2nd most on column 2 and so on.....
    # This is has been made possible due to the similarity indices
    # between the movies generated from the jupyter notebook
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

# ------------------------------------------App code ends here -------------------------------------------------------------------