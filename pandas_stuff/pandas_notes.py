import pandas as pdiddy

# this is sort of like how we create a numpy array - just here it's a series
# since pandas deals with tabulated data (csv), and not so much with matrix and linear algebra
# Serie's elements must be of the same type (homogenious) + all elements associated to a label
data = pdiddy.Series([10, 23, 56, 17])

# pandas sees everything as a 2D array (like a table), so even if you try to add more items, we 
# stay in table format (2D) in the end
# data = pdiddy.Series([[10, 23, 56, 17], [10, 23, 56, 17]])
print(data)

# If you want an actual table tho, with properties, then we need a DataFrame
# think of this as a map, where key is the column name, and the value is the values for that column
# DF are size mutable, heterogenous and support arithmetic opps.
data_many = {'Name': ['Nosferatu', 'Helen', "Chief Kief", "Diddy"], 'Age': [459, 28, 300, None], 'Gender':
['Male', 'Female', 'Male', "Unknown"]}
df = pdiddy.DataFrame(data_many)
print(df)

# statistics about DF
print(f'DF stats:\n {df.describe()}')

# Fill N/A values with smt - Remember, often with this libraries, the objects are immutable
# meaning opperations other than assignemnt opperators (like setting a specific value in a specific cell)
# will create a whole new object, that you need to assign to smt for python to save it.
df = df.fillna(0)
print(f'DF after fillna:\n {df}')

# Essentialy saying "create a new dataframe from df, but only keep rows from df where age > 30"
# under the hood df['Age'] > 30 is going to go over all the cells of the table and create a 
# new boolean 1D array/Series (mask), which will indicate which rows to keep from the DF.
df = df[df['Age'] > 30]
print(f'DF after filter:\n {df}')