import streamlit as st
import pickle
import gzip

st.set_page_config(page_title="Recommendation System", page_icon="🎬", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

def navigate_to(page_name):
    st.session_state.page = page_name

# UI for navigation
st.title("Welcome to the Multi-Recommendation System! 🎬🎮📚")
st.write("Select a Category below to get Recommendations.")

# Create buttons for navigation
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎬 Movies"):
        navigate_to("Movies")
with col2:
    if st.button("🎮 Games"):
        navigate_to("Games")
#with col3:
#   if st.button("📚 Books"):
#        navigate_to("Books")

st.divider() 


if st.session_state.page == "Movies":
    st.subheader("🎬 Movie Recommendation System")

    with gzip.open("movies_list.pkl.gz", "rb") as f:
        movies = pickle.load(f)
    with gzip.open("similar.pkl.gz", "rb") as f:
        similar = pickle.load(f)

    select_value = st.selectbox("Select a Movie", movies['Series_Title'])

    def recommend(movie):
        index = movies[movies['Series_Title'] == movie].index[0]
        distance = sorted(list(enumerate(similar[index])), reverse=True, key=lambda x: x[1])
        return [movies.iloc[i[0]].Series_Title for i in distance[1:6]]

    if st.button("Show Recommendations"):
        movie_rec = recommend(select_value)
        st.subheader("Top 5 Recommended Movies:")
        for movie in movie_rec:
            st.write(f"🎥 {movie}")

elif st.session_state.page == "Games":
    st.subheader("🎮 Game Recommendation System")

    with gzip.open("games_list.pkl.gz", "rb") as f:
        games = pickle.load(f)
    with gzip.open("game_similar.pkl.gz", "rb") as f:
        similar_games = pickle.load(f)

    select_value = st.selectbox("Select a Game", games['Title'])

    def recommend(game):
        index = games[games['Title'] == game].index[0]
        distance = sorted(list(enumerate(similar_games[index])), reverse=True, key=lambda x: x[1])
        return [games.iloc[i[0]].Title for i in distance[1:6]]

    if st.button("Show Recommendations"):
        game_rec = recommend(select_value)
        st.subheader("Top 5 Recommended Games:")
        for game in game_rec:
            st.write(f"🎮 {game}")

elif st.session_state.page == "Books":
    st.subheader("📚 Book Recommendation System")

    # Load compressed files
    with gzip.open("books_list.pkl.gz", "rb") as f:
        books = pickle.load(f)
    with gzip.open("book_similar.pkl.gz", "rb") as f:
        similar_books = pickle.load(f)

    select_value = st.selectbox("Select a Book", books['Title'])

    def recommend(book):
        index = books[books['Title'] == book].index[0]
        distance = sorted(list(enumerate(similar_books[index])), reverse=True, key=lambda x: x[1])
        return [books.iloc[i[0]].Title for i in distance[1:6]]

    if st.button("Show Recommendations"):
        book_rec = recommend(select_value)
        st.subheader("Top 5 Recommended Books:")
        for book in book_rec:
            st.write(f"📖 {book}")
