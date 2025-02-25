import streamlit as st
import pickle
import gzip

st.title("🎬 Movie Recommendation System")

# Load compressed files
with gzip.open("movies_list.pkl.gz", "rb") as f:
    movies = pickle.load(f)

with gzip.open("similar.pkl.gz", "rb") as f:
    similar = pickle.load(f)

select_value = st.selectbox("Select a Movie", movies['Series_Title'])

def recommend(movie):
    index = movies[movies['Series_Title'] == movie].index[0]
    distance = sorted(list(enumerate(similar[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [movies.iloc[i[0]].Series_Title for i in distance[1:6]]
    return recommended_movies

if st.button("Show Recommendations"):
    movie_rec = recommend(select_value)
    st.subheader("Top 5 Recommended Movies:")
    for movie in movie_rec:
        st.write(f"🎥 {movie}")
