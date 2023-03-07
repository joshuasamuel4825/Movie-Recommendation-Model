import tkinter as tk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib
#read csv into dataframe
movies = pd.read_csv('Resources/movies.csv')
#convert all columns except index to string
movies= movies.astype(str)
movies = movies.astype({'index': 'int32'})

rec_features = ['genres', 'keywords', 'popularity', 'vote_average', 'cast', 'director', 'budget']

#replacing null values
for feature in rec_features:
  movies[feature] = movies[feature].fillna('')
  
#combine all the selected features
all_features = movies['genres']+' '+movies['keywords']+' '+movies['popularity']+' '+movies['cast']+' '+movies['director']+' '+movies['budget']+' '+movies['vote_average']
vector = TfidfVectorizer(ngram_range =(1,2))
vector_features = vector.fit_transform(all_features)
similarity = cosine_similarity(vector_features)
title_list = movies['title'].tolist()

# Create the main window
window = tk.Tk()
window.title("Movie Recommender")

# Set the background color of the window
window.configure(bg="black")

window.attributes("-fullscreen", True)

title_label = tk.Label(window, text="Data Buster's Movie Recommendation System", font=("TkDefaultFont", 52, "bold"), fg="white", bg="black")
title_label.place(relx=0.5, rely=0.1, anchor="center")

question_label = tk.Label(window, text="Whats your favorite movie?", font=("TkDefaultFont", 32, "bold"), fg="white", bg="black")
question_label.place(relx=0.5, rely=0.45, anchor="center")
# Create the text box
text_box = tk.Entry(window, width=50, fg="black", bg="white")
text_box.place(relx=0.5, rely=0.5, anchor="center")

# Create the search button and its function
def search():
    try:
        printed_list = []

        list_of_all_titles = movies['title'].tolist()

        find_close_match = difflib.get_close_matches(text_box.get(), list_of_all_titles)

        close_match = find_close_match[0]

        index_of_the_movie = movies[movies.title == close_match]['index'].values[0]

        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

        print('Movies suggested for you : \n')

        i = 0
        movie_listbox.delete(0, tk.END)

        for movie in sorted_similar_movies[1:]:
            index = movie[0]
            title_from_index = movies[movies.index==index]['title'].values[0]
            if (i<5):
                printed_list.append(title_from_index)
                print(printed_list)
                i+=1
                
            
        for movie in printed_list:
            movie_listbox.insert(tk.END, movie)
    except(IndexError):
        movie_listbox.delete(0, tk.END)
        movie_listbox.insert(tk.END, "Movie Suggestions Not Available. Try A Different Movie")

search_button = tk.Button(window, text="Search", command=search)
search_button.place(relx=0.75, rely=0.5, anchor="center")

movie_listbox = tk.Listbox(window, width=50, height=10, fg="white", bg="black", font=("TkDefaultFont", 21, "bold"))
movie_listbox.place(relx=0.6, rely=0.7, anchor="center")
# Set the foreground (text) color of the window
window.option_add('*foreground', 'white')

# Set the size of the window
window.geometry("400x200")

# Start the main event loop
window.mainloop()

