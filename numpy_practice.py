import numpy as np

a = [100, 150, 200, 250, 300, 350, 400]
b = [120, 170, 220, 270, 320, 370, 420]
c = [90, 140, 190, 240, 290, 340, 390]

sales_data = np.array([a, b, c])

print(f'shape: {sales_data.shape}')
print(f'dimensions: {sales_data.ndim}')

# Task 1
# Recall: dtype is the data type of the item inside the np array
print(f'item size (in bytes): {sales_data.dtype.itemsize}')
print(f'total size (bytes): {sales_data.nbytes}') # total size of arr in bytes
print(f'total size (lenght): {sales_data.size}') # total nb of elements inside the arr
print("------------------------------\n")

# Task 2
# these are element wise opperations - they are done on each elem individually
print(f'square of each elem: {sales_data ** 2}')
print(f'increase of sales by 10%: {sales_data * 1.10}')
print(f'sales greater than 250: {sales_data > 250}')
print("------------------------------\n")

# Task 3
print(f'sales data for the first 3 days: {sales_data[:, :3]}')
print(f'sales data for product B only: {sales_data[1]}')

sales_data[2][6] = 500
print(f'modified day 7 of product C: {sales_data}')
print("------------------------------\n")

# Task 4
print(f'total sales across all products: {sales_data.sum()}')
# alternative to the previous
# print(f'total sales across all products: {np.sum(sales_data)}')
print(f'avg sales for each product: {np.average(sales_data, axis=1)}') # axis=1 -> rows
print(f'max product sale on a single day: {np.max(sales_data, axis=0)}') # axis=0 -> cols
print("------------------------------\n")

# Task 5
print(f'sales adjustment placeholder: {np.zeros((3,3), dtype=np.int64)}')
print(f'identity matrix: {np.eye(4,4)}')
print(f'sales forecast (random): {np.random.random((2,3))}')

# same as above, syntax different tho - here we dont pass a tuple for the shape, rather we pass each dimension 
# size one by one
# print(f'sales forecast (random): {np.random.rand(2,3)}')
print("------------------------------\n")

# Task 6
print(f'sales timestamps: {np.linspace(1, 12, num=12, dtype=np.int64)}')
print(f'sine transformation: {np.sin(sales_data[0])}') # note that this is a element wise opperation!