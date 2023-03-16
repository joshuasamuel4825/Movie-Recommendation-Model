# Movie-Recommendation-Model

## Project Overview

Movie recommendation models using machine learning are becoming increasingly popular because they provide a personalized experience to users. In today's digital age, users have access to an overwhelming number of movies, TV shows, and other video content. With so much content available, it can be difficult for users to find something they want to watch. Recommendation systems use machine learning algorithms to analyze users' viewing history, preferences, and other data to provide tailored recommendations. By providing personalized recommendations, these models can help users discover new content they may not have found otherwise, improving their overall experience and engagement with the platform.

## Project Structure

For this project, we used a dataset that has over 5000 movies with over 20 columns with that has different information about the movie. We then cleaned the data and used relevant features to create a machine learning model to recommend movies. After creating the machine learning mode, a UI was created so a user could input a movie to recieve a recommendation.

## Project Contributors

- Annalyse Bergman
- Sarah Beck
- Joshua Samuel
- Timea Jakab
- Yi Lu

# Objective

Create a machine learning model that recommends a user movies based on features such as genre, runtime, director, cast, etc. Create a UI for the model so user can input favorite movie to get the recommendation.

# Methodology
## Extract
For this project, we worked with one large dataset that had over 20 features such as genre, runtime, cast, director, title, tags, etc.
* We extracted the dataset from the TMDB website and it was a csv file with over 5000 rows and 25 columns. After downloading the dataset, we loaded them into a pandas dataframe using Python and Jupyter Notebook.

## Transform
* The original dataset had over 20 columns and most of them unnecessary to the machine learning model. We removed the extra columnns and only kept columns that would provide significant value to our model. The columns we kept were: 'genres', 'keywords', 'popularity', 'vote_average', 'cast', 'director', and  'budget'.
* We then filled null values from the dataframe to get better results.
* After cleaning the data, we combined all the features together into text data and turned that data into a matrix.

## Machine Learning Model
The machine learning model was created using cosine similarity and similarity scores were given to each movie based on the selected features. The movies with the highest similarity scores are then shown as recommendations to the user.

## User Interface
The user interface for the model is in the app.py file and is built using the python library, tkinter. It has one textbox where the user can input a movie title and then a search button which will activate the model to recommend 5 movies which will be listed below the textbox.

##References
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv



