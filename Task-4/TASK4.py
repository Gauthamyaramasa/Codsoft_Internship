import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load movies and ratings data
movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')

# Randomly select 60% of the ratings data
sampled_ratings_df = ratings_df.sample(frac=0.4, random_state=42)

# Merge the data to create a user-item rating matrix
user_item_matrix = sampled_ratings_df.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Calculate item-item similarity using cosine similarity
item_similarity = cosine_similarity(user_item_matrix.T)

# Function to get item recommendations for a movie
def get_movie_recommendations(movie_name, num_recommendations=5):
    # Find the movieId for the given movie name
    movie_id = movies_df[movies_df['title'] == movie_name]['movieId'].values[0]
    
    # Get the similarity scores for the specified movie
    movie_scores = item_similarity[movie_id]
    
    # Create a Pandas Series for movie scores
    movie_scores_series = pd.Series(movie_scores, index=user_item_matrix.columns)
    
    # Sort movies by score and recommend top movies
    recommended_movie_ids = movie_scores_series.sort_values(ascending=False).head(num_recommendations)
    
    # Get the titles of recommended movies
    recommended_movies = movies_df[movies_df['movieId'].isin(recommended_movie_ids.index)]['title']
    
    return recommended_movies

#Getting recommendations for a movie by inputting its name
input_movie_name = "To Die For (1995)"
recommended_movies = get_movie_recommendations(input_movie_name)
print("Recommended movies for", input_movie_name, ":")
print(recommended_movies)