# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:26:01 2022

@author: HI
"""

# Importing necessary libraries 

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Read csv file
Fifa_23 = pd.read_csv("Fifa 23 Fut Players.csv", index_col = False)
print(Fifa_23)

# Describe data for each feature
Fifa_23.describe()

# Using info to get information about the dataset
Fifa_23.info()

# Analyzing missing values
Fifa_23.isnull().sum()

# Dropping missing values
Fifa_23 = Fifa_23.dropna()
Fifa_23.isnull().sum()

# calling out all the columns
Fifa_23.columns

# Renaming the 'Name' column
Fifa_23.rename(columns={'Name':'Players'}, inplace= True)
Fifa_23_copy = Fifa_23.copy()
print(Fifa_23_copy)

# Plotting lines for the first 20 rows
Fifa_23_foot = Fifa_23_copy.iloc[:8,:]
print(Fifa_23_foot)

# Defining functions for the multiple line plot
def line_plot(x_axis, my_list, label, title):
    plt.figure(figsize = (12,9))
    for i in range(len(my_list)):
        plt.plot(x_axis, my_list[i],label = label[i])
    plt.legend()
    plt.title(title, fontsize = 12)
    plt.show()
    
# Parameters for the multiple line plot    
x_axis = Fifa_23_foot['Players']
my_list = [Fifa_23_foot['Popularity'], Fifa_23_foot['BS'], Fifa_23_foot['DRI'], Fifa_23_foot['SHO']]
label = ['Popularity', 'Base stats', 'Player Dribble', 'Player shooting power']
title = 'Line plot of Players showing some of their skills'
line_plot(x_axis, my_list, label, title)


# Defining functions for the barchart
def bar_chart(x_axis, y_axis, title):
    plt.figure(figsize=(12,9))
    plt.bar(x_axis, y_axis, color= None)
    plt.xlabel('Players', fontsize= 12)
    plt.ylabel('Ratings', fontsize= 12)
    plt.title(title, fontsize= 12)
    plt.show()
    return

# Parameters for the Barchart
x_axis = Fifa_23_foot['Players']
y_axis = Fifa_23_foot['Ratings']
title = 'Bar Chart showing the Best Ratings of Players'
bar_chart(x_axis, y_axis, title)


# sum up players by country to produce a subplot pie
Players_group = Fifa_23_foot.groupby('Country')[['Popularity', 'BS', 'DRI', 'SHO']].sum()
print(Players_group)

# Defining functions for Subplot Pie chart
def subplot_pie_chart(x_axis, label, title):
    plt.figure(figsize=(15,10))
    for i in range(len(x_axis)):
        plt.subplot(2,2,i+1).set_title(title[i])
        plt.pie(x_axis[i],labels=label)
    plt.show()

# Parameters for the subplot piechart    
x_axis = [Players_group['Popularity'],Players_group['BS'],Players_group['DRI'],Players_group['SHO']]
label = Players_group.index
title = ['Popularity', 'Base stats', 'Player Dribble', 'Player shooting power']
subplot_pie_chart(x_axis, label, title)   