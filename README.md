🎬🎮 Movie & Game Recommendation System

📌 Overview

This is a Movie & Game Recommendation System built using Streamlit and Machine Learning techniques. The application allows users to select either movies or games and get personalized recommendations based on similarity scores.

🚀 Features

Movie Recommendations: Get similar movie recommendations based on your selection.

Game Recommendations: Find games related to your favorite ones.

Interactive UI: Users can switch between Movies and Games using buttons.

Optimized Data Handling: Uses compressed pickle files (.pkl.gz) for efficient data storage and loading.

🛠️ Tech Stack

Python 🐍

Streamlit 🌟 (for UI)

Pandas (for data processing)

Pickle + Gzip (for optimized storage)

Scikit-learn (for similarity calculations)

📂 Project Structure

Recomendation_Bot/
│── app.py               # Main Streamlit app
│── pages/               # Folder for separate pages (Movies & Games)
│── database/            # Raw datasets
│── models/              # Machine learning models
│── movies_list.pkl.gz   # Compressed Movie Data
│── similar.pkl.gz       # Compressed Similarity Matrix
│── games_list.pkl.gz    # Compressed Game Data
│── games_similar.pkl.gz # Compressed Similarity Matrix
│── README.md            # Project Documentation

🔥 How to Run

Clone the Repository:

git clone https://github.com/yashjain71288/Recomendation_Bot.git

Navigate to the Project Folder:

cd Recomendation_Bot

Install Dependencies:

pip install -r requirements.txt

Run the Streamlit App:

streamlit run app.py

Select 'Movies' or 'Games' and Get Recommendations!

⚡ Future Enhancements

Add Book Recommendations 📚 (Coming Soon)

Improve UI with better design and animations

Optimize ML model for better accuracy

📜 License

This project is open-source and free to use. Feel free to contribute! 🚀

