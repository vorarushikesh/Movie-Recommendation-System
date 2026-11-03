import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os
import gdown

session = requests.Session()

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
}

FALLBACK_POSTER = "https://via.placeholder.com/500x750?text=No+Poster"

def fetch_poster(movie_id):
    try:
        url = (
            f"https://api.themoviedb.org/3/movie/{movie_id}"
            f"?api_key=960b5f6a35d8cda952423d397cd42a75"
        )
        response = session.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return FALLBACK_POSTER
    except Exception as e:
        print(f"[fetch_poster] movie_id={movie_id} → {e}")
        return FALLBACK_POSTER


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters


movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

if not os.path.exists("similarity.pkl"):
    gdown.download(
        id="1EzF9viNSF1j329M1E_GQOl1HEhknSg9x",
        output="similarity.pkl",
        quiet=False
    )
    
similarity = pickle.load(open("similarity.pkl", "rb"))

st.header("Movie Recommendation System")

selected_movie_name = st.selectbox("Enter movie name", movies["title"].values)

if st.button("Recommend"):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie_name)

    cols = st.columns(len(names))
    for i in range(len(names)):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
