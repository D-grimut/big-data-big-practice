import numpy as np

python_list = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
print(python_list)

# a = np.array([1, 2, 3, 4, 5]) # shape = (5,)
a = np.array([(1, 2, 3, 4, 5), [1, 2, 3, 4, 5], [1, 2, 3, 4, 5] ]) # shape = (3, 5)
a2 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) # shape = (2, 5)
b = a ** 2
c = np.sum(a) # same as c = b.sum()

print("shape a: ", a.shape)
print("shape a2: ", a2.shape)

print(b, c)
rows, cols = a.shape
print(rows, cols)
print(a)
print(type(a))

print("--------")

# a = a.reshape(1, 15)
print("hehe", a)

# note: when reshaping, the number of elements should be the product of rows * cols
# so a reshape of an arangment of 25 elemnets into a matrix of size 2x2 wont work since 2x2 = 4
d = np.arange(24).reshape(2,2,6)
print(d.dtype)

e = np.full((2, 2), 7, dtype=np.int8)
print("The full array:", e)
print(e.dtype.itemsize)

f = np.eye(10)
print("The 3x3 identity matrix:", f)

# Create a random array
print("The random array:", np.random.random((2, 4)))

print(np.array_equal(a, a2))

# note that axis=0 -> col, axis=1 -> row
# note: if we ommit the axis we perform the operation on all elements in the matrix, as if we flattened the matrix into size (1, n) - 1 row x n columns
# suming by columns - num of columns remains the same, but now we only have one (1) row
print(a.sum(axis=0))
print("Sum of all:", a.sum())

# suming by rows - we have one row at the end, where the num of columns is the number of rows we had (the value at each col is the sum of that row)
print(a.sum(axis=1))

# suming by row - but the value at index i in a row, is the sum of all numbers up to and including i
# the shape after cumsum remains the same, BUT if we sum along the rows (axis 1), we have the cumsum appear in the rows
# and if we do columns (axis 0), the cumsum will appear in the collumns.
print("cumsum:", b.cumsum(axis=0)) 

# Note: new_a = old_a simply assigns a new REFERANCE to the array old_a.
# however, doing new_a = old_a.view() will create a new object (a view of the array), that will point to the values of old_a, sort of like a shared pointer in itself is a unique entity, but points to a shared resource.

c = np.array([[5, 2], [7, 6]])
c.sort(axis=1)
print(c) 


b_new = np.array([[1.5, 22, 3], [4, 55, 6], [-1,-1,-1]])
print(b_new[0:2, 1]) # Extracts second column - we get the first two rows with [0:2] and then acess the first column with [1], note that the result of this is a 1D array, since we are getting all the values inside the 2nd column, of the first two rows
print(b_new[:1]) # Extracts first row

# Boolean indexing - creates boolean mask and returns all items that have "True" in the boolean mask
print(b_new[b_new < 3]) # output: [ 1.5 -1.  -1.  -1. ]

# Here we are simply passing in the matrix of indeces of the items we want
# so, we want the item at row 1, col 1, and row 0, col 0
print(b_new[[1, 0], [1, 0]])


