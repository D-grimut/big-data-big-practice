import pandas as pdiddy
import numpy as np

# this is sort of like how we create a numpy array - just here it's a series
# since pandas deals with tabulated data (csv), and not so much with matrix and linear algebra
# Serie's elements must be of the same type (homogenious) + all elements associated to a label
data = pdiddy.Series([10, 23, 56, 17])

# Another example
ser = pdiddy.Series([100, 200, 300, 400], index=['apple', 'ball', 'cat', 'dog'])
print(ser)
print(ser * 2) # ELEMENET wise opperation

# acessing by ser.loc vs ser[...] => loc if (inclusive, inclusive) for slicing and ser[...] is (inclusive, exclusive)

# Series =  A one-dimensional labeled array
# DF = A two-dimensional labeled data structure similar to a table
# data = pdiddy.Series([[10, 23, 56, 17], [10, 23, 56, 17]])
print(data)

# If you want an actual table tho, with properties, then we need a DataFrame
# think of this as a map, where key is the column name, and the value is the values for that column
# DF are size mutable, heterogenous and support arithmetic opps.
data_many = {'Name': ['Nosferatu', 'Helen', "Chief Kief", "Diddy"], 'Age': [459, 28, 300, None], 'Gender':
['Male', 'Female', 'Male', "Unknown"]}
# df = pdiddy.DataFrame(data_many, index=["old romanian", "wierd british girl", "OG rapper", "we dont like him"])
df = pdiddy.DataFrame(data_many)
print(df)
print("--------------------")

print(f'names here:\n{df["Name"]}') # Select column
print(df.loc[0]) # Select row by index - the index is the LABEL, in this case Label=Index of the row
print(f'iloc with arr: {df.iloc[0, 1]}') # Select element by position - row 0, col 1
print(df[1:3]) # Slice rows - note we cannot slice rows and columns - need to use iloc, or loc for that
print(df.loc[:, 'Name':'Age']) # Slice rows and columns

print("--------------------")
# Data frames can be build from many things: ndarray, Series, map, lists, dict, constants, or another DataFrame.
data_ndarr = np.array(["p", "diddy"])
df_diddy = pdiddy.DataFrame(data_ndarr)
print(f'boo: {df_diddy}')

# statistics about DF
print(f'DF stats:\n {df.describe()}')

# Fill N/A values with smt - Remember, often with this libraries, the objects are immutable
# meaning opperations other than assignemnt opperators (like setting a specific value in a specific cell)
# will create a whole new object, that you need to assign to smt for python to save it.
df = df.fillna(0)
print(f'DF after fillna:\n {df}')

# Essentialy saying "create a new dataframe from df, but only keep rows from df where age > 30" - CREATES A NEW DF
# under the hood df['Age'] > 30 is going to go over all the cells of the table and create a 
# new boolean 1D array/Series (mask), which will indicate which rows to keep from the DF.
df_bool = df[df['Age'] > 30]
print(f'DF after filter:\n {df_bool}')

# df[['Age']] -> returns a DF
# df['Age'] -> returns a Series

# # summariszing data using groupby
grouped = df.groupby('Age')
print(grouped)

# Concatenation: pd.concat([df1, df2]) = append df2 to the side/bellow of df1
# Merging: pd.merge(df1, df2, on='key') = similar to the SQL JOIN - merges on some key