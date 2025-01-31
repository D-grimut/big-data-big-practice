import pandas as pd

# reading data from the CSV as a DF
movies = pd.read_csv('/Users/danielgrimut/Downloads/ml-32m/movies.csv')

# parse_dates parses the timestamps into actual date-time format
# ratings = pd.read_csv('/Users/danielgrimut/Downloads/ml-32m/ratings.csv', parse_dates=['timestamp'])

ratings = pd.read_csv('/Users/danielgrimut/Downloads/ml-32m/ratings.csv')
# tags = pd.read_csv('/Users/danielgrimut/Downloads/ml-32m/tags.csv')
# print(movies.head())
print(ratings.head())

# merging stuff - coemmenetd out for performance reasons
# movies_with_tags = pd.merge(movies, ratings, on='movieId')
# print(movies_with_tags.head())

print("ratings DF without timestamp col")
del ratings["timestamp"] # this approach is primarily used to delte cols in pandas
print(ratings.head())

print(f'select row 0 (by index) of ratings {ratings.iloc[0]}')
print(f'select row 0 (by label) of ratings {ratings.loc[0]}')
print(f'check if "ratings" is in row: {"ratings" in ratings.loc[0]}')

# renaming a series - recall when we have a singular row, then it's nothing more than a 1D array = Series
row_0 = ratings.loc[0].rename('first_row')
print(row_0.name) # Output: 'first_row'

# Identifies the most frequently occurring values for each column.
print(f'what is the mode for "ratings"?\n {ratings.mode()}')

filter_2 = ratings.loc[ratings['rating'] > 0]
# The mean() here will agregate ALL the columns inside the DF - so we regroupped by movieID
# and for each group aggregate (take the mean) of all remaining columns - so if one column would to be
# a string, we need to handle that by setting numeric_only=True
print(f'movie mean score: {filter_2.groupby("movieId").mean()}')

# is_animation is a Series (1D array) indicating the rows to keep.
is_animation = movies['genres'].str.contains('Animation')
print(movies[is_animation].head(15))
print(is_animation)
print("-----------------")

average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
id_movie = average_rating.loc[average_rating["rating"] == 5.0].index
# Same as the line before - notice how we can acess ratings using dot notation (like a property) and as a string "key"
# id_movie = average_rating.loc[average_rating.rating == 5.0].index
print(id_movie)
print(movies.loc[movies.movieId.isin(id_movie)].head())