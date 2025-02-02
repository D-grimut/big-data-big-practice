import matplotlib.pyplot as plt
import numpy as np
import pandas as pdd

dataset = pdd.read_csv("dataset.csv")

# select ny - sort by month
ny_df = dataset[dataset["City"] == "New York"].sort_values(by="Month")
print(ny_df)

fig, axs = plt.subplots(3, 2, figsize=(10, 8))

# task 2
months = ny_df["Month"].to_numpy(dtype=np.int32)
revenue = ny_df["Revenue"].to_numpy(dtype=np.int32)

# PROPER WAY TO DO SUBPLOTS
axs[0,0].plot(months, revenue, linestyle = "-", label='Revenue vs Months in NY', color='black', marker='x')
axs[0,0].grid()
axs[0,0].set_xlabel("Month")
axs[0,0].set_ylabel("Revenue")
# plt.show()

# task 3
# explore take the list of categories, and makes each category its own row
categories = ny_df["Product Categories"].str.split(",").explode('Product Categories_y')
categories_ny = pdd.merge(ny_df, categories, left_index=True, right_index=True)
# print(categories_ny)

# reset_index makes the series back into a DF
categories_price = categories_ny.groupby('Product Categories_y')["Revenue"].sum().reset_index()
# print(categories_price)

categories_fixed = categories_price['Product Categories_y'].to_numpy()
categories_revenues = categories_price['Revenue'].to_numpy()

axs[0, 1].bar(categories_fixed, categories_revenues, width=0.5, color="blue")
axs[0, 1].grid()
axs[0, 1].set_xlabel("Categories")
axs[0, 1].set_ylabel("Revenue")
axs[0, 1].set_title("Categories vs Revenue in NY")
# plt.show()

# task 4 - this task SHOULD be done using for loop, since we don't know how many total cities we have
ny_scatter_x = ny_df['Revenue']
ny_scatter_y = ny_df['Number of Transactions']

# making size proportional to money per transaction
rev_per_trans_ny = ny_scatter_x * 10 / ny_scatter_y

px_df = dataset[dataset["City"] == "Phoenix"].sort_values(by="Month")
px_scatter_x = px_df['Revenue']
px_scatter_y = px_df['Number of Transactions']

rev_per_trans_px = px_scatter_x * 10/ px_scatter_y

axs[1, 0].scatter(ny_scatter_x, ny_scatter_y, color='blue', s=rev_per_trans_ny)
axs[1, 0].scatter(px_scatter_x, px_scatter_y, color='red', s=rev_per_trans_px)

axs[1, 0].grid()
axs[1, 0].set_xlabel("Revenue")
axs[1, 0].set_ylabel("Number of Transactions")
axs[1, 0].set_title("Categories vs Revenue in NY")
# plt.show()

# task 5
tot_rev = dataset.groupby(by="City")['Revenue'].sum().reset_index()
total_rev = tot_rev['Revenue'].sum()

cities = tot_rev['City']
rev = tot_rev['Revenue']

# how to explode - start with empty explode, and then populate it with which ones you want to explode
explode = [0] * len(rev)  # Start with no explosion
max_contrib_index = rev.idxmax()  # Find the index of the largest contributor
explode[max_contrib_index] = 0.1  # "Explode" the largest contributor

# element wise opp
rev = (rev / total_rev) * 100

axs[1, 1].pie(rev, labels=cities, explode=explode, shadow=True)
# plt.show()

# task 6
axs[2,0].hist(dataset['Customer Satisfaction Score'], bins=10, edgecolor='black')

# Adding titles and labels
axs[2,0].set_title('Customer Satisfaction Scores Across All Cities')
axs[2,0].set_xlabel('Satisfaction Score')
axs[2,0].set_ylabel('Frequency')

plt.suptitle("hell yeah analysis")
plt.show()