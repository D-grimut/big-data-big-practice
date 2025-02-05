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

# Creating a new column and giving it the values of True or false -> we are assocaited a SERIES to the column
# the Series = values in the column
movies["IsComedy"] = movies["genres"].str.contains("Comedy")
print(f'Movies with Comedy column:\n{movies.head()}')
print("-----------------------------")

# Task 3
print(f'Movies stats:\n{movies.describe()}')

# when selecting a column (ratings["rating"]) we are interacting with a Series object (1D array)
print(f'Most Frequent Rating:{ratings["rating"].mode()}')

# reset_index resets the index of the Series produced, and names the series 'rating'.
# the double brackets for [["rating"]] mean we are selecting "rating" col and making it into a DF
avg_rating_movies = ratings.groupby(by="movieId")[["rating"]].mean()
print(f'Avg Rating for each movie:\n{avg_rating_movies}')

best_movies = avg_rating_movies[avg_rating_movies["rating"] == 5.0]
print(f'Movies with rating of 5:\n{best_movies}')

ratings["timestamp"] = pdd.to_datetime(ratings["timestamp"], unit="s")
ratings = ratings[ratings["timestamp"] > "2015-02-01"]
print(f'Ratings timestamp converted:\n{ratings.sort_values(by="timestamp")}') # by default, sort is ascending
print("-----------------------------")

# Task 4
movies_with_tags = pdd.merge(movies, tags, on='movieId')
print(f'Movies with tags:\n{movies_with_tags}')

box_office = pdd.merge(movies_with_tags, avg_rating_movies, on='movieId')
animation = box_office[box_office["tag"] == 'animation']
print(f'Box Office - Animation:\n{animation}')

comedies = box_office[(box_office["rating"] >= 4.0) & (box_office["IsComedy"])]
print(f'Good Comedies:\n{comedies.sort_values(by="rating")}')
print("-----------------------------")

# Task 5
# Extracting the years from the movie title and placing that into a column called "year"
movies_with_year = pdd.merge(movies, avg_rating_movies, on='movieId')
movies_with_year["year"] = movies_with_year["title"].str.extract(r"\((\d{4})\)").astype(float)
print(f'Movies with years:\n{movies_with_year}')

# all we need for the correlation is the two columns that we are interested of finding the correlation of
correlation = movies_with_year["year"].corr(movies_with_year["rating"])
print("Correlation between release year and average rating:", correlation)

# Again, here we want to group by year and avergae the ratings - this means we need to 
# select the "rating" column AFTER the groupby, and then mean, otherwise the mean() will be performed
# on all the columns present in the groupby.

# since we aggregate by year, we gurantee that the new DF created will have unique labels for year - year is our new index here
yearly_avg = movies_with_year.groupby(by="year")[["rating"]].mean()
yearly_avg.rename(columns={"rating": "avg_yearly_rating"})
# Throws a key error since our labels are the years - 0 is not in the "year" list
# print(f'item: {yearly_avg.loc[0]}')
print(f'Avg yearly rating:{yearly_avg}')
print("-----------------------------")