# Movie Recommendation System

A movie recommendation web application built with **Python** and **Streamlit**. Select a movie from the dropdown and the application recommends five similar movies. It also retrieves movie poster images from **The Movie Database (TMDB) API**.

## Features

- Select a movie by title.
- Get five movie recommendations based on the precomputed similarity data.
- Display poster images for recommended movies.
- Show a fallback image when a poster cannot be retrieved.
- Retry selected temporary TMDB API errors when fetching poster information.

## Tech stack

- Python
- Streamlit
- Pandas
- Requests
- urllib3
- Pickle files containing the movie data and precomputed similarity values
- TMDB API for movie poster information

## Project structure

Keep the application file, dependency file, and both model/data files in the project root:

```text
Movi Recommended system/
├── .gitignore
├── README.md
├── requirements.txt
├── movie_recommended_system.py
├── movie_dict.pkl
└── similarity.pkl
```

The application expects these exact filenames:

- `movie_dict.pkl`
- `similarity.pkl`

Do not rename these files unless you also update the paths in `movie_recommended_system.py`.

## Run the project on your computer

### 1. Keep the project files together

Make sure these files are in the same folder:

- `movie_recommended_system.py`
- `movie_dict.pkl`
- `similarity.pkl`
- `requirements.txt`

### 2. Open the project folder

Open the `Movi Recommended system` folder in VS Code. Open the VS Code terminal in that folder.

### 3. Install the required libraries

Run this command in the terminal:

```bash
pip install -r requirements.txt
```

### 4. Add your TMDB API key

The app reads your TMDB API key from an environment variable. In the VS Code PowerShell terminal, run this command. Replace the example text with your own TMDB API key:

```powershell
$env:TMDB_API_KEY="your_tmdb_api_key"
```

Do not put your real API key in this README file or upload it to GitHub.

### 5. Run the app

Run this command:

```bash
streamlit run movie_recommended_system.py
```

Streamlit will show a local address in the terminal. Open that address in your web browser.

project url : https://movie-recommendation-system-ouiz.onrender.com/

## Note

Keep `movie_dict.pkl` and `similarity.pkl` in the same folder as `movie_recommended_system.py`. The app needs both files to recommend movies.
