import streamlit as st
import pickle
import gzip

st.title("🎮 Game Recommendation System")

with gzip.open("games_list.pkl.gz", "rb") as f:
    games = pickle.load(f)

with gzip.open("games_similar.pkl.gz", "rb") as f:
    similar_games = pickle.load(f)

select_value = st.selectbox("Select a Game", games['title'])

def recommend(game):
    index = games[games['title'] == game].index[0]
    distance = sorted(list(enumerate(similar_games[index])), reverse=True, key=lambda x: x[1])
    recommended_games = [games.iloc[i[0]].title for i in distance[1:6]]
    return recommended_games

if st.button("Show Recommendations"):
    game_rec = recommend(select_value)
    st.subheader("Top 5 Recommended Games:")
    for game in game_rec:
        st.write(f"🎮 {game}")
