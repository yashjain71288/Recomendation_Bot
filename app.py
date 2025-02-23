import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl", 'rb'))

st.header("Recomendation System")
st.selectbox("Select Movies from Dropdown", movies)

if st.button("Show Recomended"):
    pass
