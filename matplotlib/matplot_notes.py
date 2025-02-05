import matplotlib.pyplot as plt
import numpy as np

# Note: see matplot_practice_a1.py for PROPER WAY TO DO SUBPLOTS

# Data - can be represneted as: list, tuple, or NumPy array AND Series

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

x1 = [0, 5]
y1 = [20,0]

# creates a plot - we still need to define the axesis and such
# for a grapth to be valid, x and y MUST have the same shapes (same num of items)
# use common sence, if you can't make (x,y) pairs then you can't plot the data points.
# If y is omitted, the function assumes values starting from 0 for the x-axis and
# takes x as the y-values
plt.plot(x, y, linestyle = "--",label='Linear Growth', color='blue', marker='x')

# If I remove x, the indeces of the y list are the x values
# plt.plot(y, linestyle = "--",label='Linear Growth', color='blue', marker='x')

# we are using fmt syntax - 'o:r' = 'o' marker, ':' for dotted line and 'r' for red
plt.plot(x1, y1, 'o:r', label="slibidi", ms=20, mfc='black', linewidth=5) # ms = marker size, mfc=marker color

# Specifying the font dict that will contain the font info
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

# Add labels and title
plt.xlabel("Overs", fontdict=font1)
plt.ylabel("Runs", fontdict=font2)
plt.title('Basic Line Plot', loc="left")
plt.suptitle("Im just a chill guy")

# Add legend
plt.legend()

# Can customize the gridlines the same way we customize lines - fmt syntax doesnt work here
plt.grid(color="yellow", linestyle="--")
plt.subplot(2,3,1) # for Subplot to work, you need to define ONCE the dimension of the grid, and then just place stuff in each time you create a new plot; make sure plot ID is different

# scatter
mycolor = ['red', 'green', 'purple', 'lime', 'aqua']
size = [10, 60, 120, 80, 20]
plt.scatter(x, y, color=mycolor, s=size, alpha=0.5) # alpha = transparency
plt.subplot(2,3,2)

# bar
x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])
plt.bar(x, y,  width=0.5)
plt.subplot(2,3,3)

# histogram
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.subplot(2,3,4)

# pie chart
x = np.array([35, 25, 25, 15])
explode = [0.2, 0, 0, 0]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
plt.pie(x, labels=labels, explode=explode, shadow=True)
plt.subplot(2,3,5)

# Display the plot - sort of like spark where computation doesn;t start until a specific command fire out
plt.show()

# If I were to start another plt after this, it will create a new plot, that will be placed onto
# the canvas once I call plt.show() - if I try to make more plots before plt.show(), they will
# be placed onto the same plot.