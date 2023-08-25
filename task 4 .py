Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Movie ratings matrix (rows: users, columns: movies)
ratings = np.array([
    [5, 4, 0, 0, 3, 0],
    [0, 0, 5, 4, 0, 0],
    [4, 5, 0, 0, 2, 3],
    [0, 3, 4, 0, 0, 5],
    [0, 0, 3, 5, 4, 0]
])

... # Calculate the cosine similarity between users
... user_similarity = cosine_similarity(ratings)
... 
... # Function to recommend movies to a user
... def recommend_movies(user_id, num_recommendations=3):
...     user_ratings = ratings[user_id]
...     similar_users = np.argsort(user_similarity[user_id])[::-1]
...     
...     recommended_movies = []
...     for i in range(len(ratings[user_id])):
...         if user_ratings[i] == 0:
...             similar_user_ratings = ratings[similar_users[i]]
...             recommended_movies.append(np.argmax(similar_user_ratings))
...             
...         if len(recommended_movies) == num_recommendations:
...             break
...             
...     return recommended_movies
... 
... def main():
...     num_users, num_movies = ratings.shape
... 
...     print("Welcome to the Movie Recommendation System!")
... 
...     while True:
...         user_id = int(input("Enter your user ID (0 to {}): ".format(num_users - 1)))
...         if user_id < 0 or user_id >= num_users:
...             print("Invalid user ID. Please try again.")
...             continue
...         
...         recommendations = recommend_movies(user_id)
...         
...         print("Recommended movies for user", user_id)
...         for i, movie_id in enumerate(recommendations):
...             print(f"{i + 1}. Movie {movie_id}")
... 
...         another_recommendation = input("Do you want another recommendation? (y/n): ")
...         if another_recommendation.lower() != 'y':
...             print("Thank you for using the Movie Recommendation System!")
...             break
... 
... if __name__ == "__main__":
...     main()
... 
