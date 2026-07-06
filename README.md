 Movie Recommender System

#Live Demo
https://movierecommendersystembyleelamajji-t9byzxhq9qowzzvgoy9qny.streamlit.app/
#Project Overview
This project is a Content-Based Movie Recommender System that suggests similar movies based on user input.
The system analyzes movie metadata such as genres, keywords, cast, crew, and overview to find similarities between movies.
When a user selects a movie, the system recommends the top similar movies.

#Key Features
- Search any movie
- Get top recommended movies instantly
- Content-based similarity matching
- Interactive Streamlit web application

#Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Cosine Similarity

#Dataset Features
The model uses movie information such as:
- Movie ID
- Title
- Overview
- Genres
- Keywords
- Cast
- Crew (Director)
- Popularity

#Machine Learning Workflow
1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Engineering (tags creation)
4. Text Vectorization using CountVectorizer / TF-IDF
5. Cosine Similarity Calculation
6. Model Saving using Pickle
7. Streamlit UI Development
8. Recommendation Generation

#Model Used
Content-Based Filtering using Cosine Similarity
Saved files:

similarity.pkl
movie_dict.pkl
movies.pkl
