import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl", 'rb'))
similar = pickle.load(open("similar.pkl", 'rb'))

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide")



st.header("Movie Recomendation System")
select_value = st.selectbox("Select Movies from Dropdown", movies)


def recommend(movie):
    index = movies[movies['Series_Title']==movie].index[0]
    distance = sorted(list(enumerate(similar[index])), reverse = True, key = lambda vector:vector[1])
    recommend_movie=[]
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].Series_Title)
    return recommend_movie
    



if st.button("Show Recomended"):
    movie_rec = recommend(select_value)
    col1, col2, col3, col4, col5=st.columns(5)
    with col1:
        st.text(movie_rec[0])
    with col2:
        st.text(movie_rec[1])
    with col3:
        st.text(movie_rec[2])
    with col4:
        st.text(movie_rec[3])
    with col5:
        st.text(movie_rec[4])
        
