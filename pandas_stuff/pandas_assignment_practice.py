import pandas as pdd

# reading data from the CSV as a DF
movies = pdd.read_csv('/Users/danielgrimut/Downloads/ml-32m/movies.csv')
ratings = pdd.read_csv('/Users/danielgrimut/Downloads/ml-32m/ratings.csv')
tags = pdd.read_csv('/Users/danielgrimut/Downloads/ml-32m/tags.csv')

# Task 1
print(f'First five movies:\n {movies.head()}')
print(f'First five ratings:\n {ratings.head()}')

# Same as numpy
print(f'Shape of movies DF:\n {movies.shape}')
print(f'Shape of ratings DF:\n {ratings.shape}')

# The "any()" simply checks for each column if at least one item is null
# in this case True = an item is null
print(f'Missing data:\n{movies.isnull().any()}')
print(f'Missing data Tags:\n{tags.isnull().any()}')

tags = tags.dropna()
print(f'Missing data Tags:\n{tags.isnull().any()}')
print("-----------------------------")

# Task 2
genres_split = movies['genres'].str.split('|', expand=True)
print(f'Genres split:\n {genres_split}')

# Creating a new column and gicing it the values of True or false -> we are assocaited a SERIES to the column
# the Series = values in the column
movies["IsComedy"] = movies["genres"].str.contains("Comedy")
print(f'Movies with Comedy column:\n{movies.head()}')
print("-----------------------------")

# Task 3
print(f'Movies stats:\n{movies.describe()}')

# when selecting a column (ratings["rating"]) we are interacting with a Series object (1D array)
print(f'Most Frequent Rating:{ratings["rating"].mode()}')

# reset_index resets the index of the Series produced, and names the series 'rating'.
avg_rating_movies = ratings.groupby(by="movieId")["rating"].mean().reset_index(name="rating")
print(f'Avg Rating for each movie:\n{avg_rating_movies}')

best_movies = avg_rating_movies[avg_rating_movies["rating"] == 5.0]
print(f'Movies with rating of 5:\n{best_movies}')
print("-----------------------------")