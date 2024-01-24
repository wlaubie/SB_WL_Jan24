####### Spring Board

####### 3.2 - Lists

#Ex 1: List Addition

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
area_1 = areas + ["poolhouse",24.5]
print(area_1)

# Add garage data to areas_1, new list is areas_2
area_2 = area_1 + ["garage",15.45]
print(area_2)

#Ex 2: List Deletion

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# How to delete poolhouse
del(areas[-4:-2])
print(areas)

#Ex 2: Make sure areas_copy does not affect areas (original)

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas) #trick is adding list() in front

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)

#Ex 3: List Functions

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

import numpy as np
print(np.__version__)

print(np.array([1,2,3]))


###### Matlib

#Ex1: Practice
import matplotlib.pyplot as plt

year = [1950,1970,1990,2010] #X Axis
pop = [2.519,3.692,5.263,6.972]         #Y Axis

plt.scatter(year,pop)
plt.show()
#plt.close()

#Ex 2: Data Visualisation

#a) sample plot
import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3]
y = [1,4,9]
z = [10,5,0]

plt.plot(x,y)
plt.plot(x,z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y & z")
plt.legend(["this is y", "this is z"]) #only refer to y/z plotting as x is same for both


plt.show()

#b) Retrieve data from csv file

sample_data = pd.read_csv("sample_data.csv")
print(sample_data)

#lets say you are now interested to retrieve data from a specific column or cell

print(sample_data.column_c.iloc[2]) #this will return 3rd element of column C

#c) Plot from retreive data

plt.plot(sample_data.column_a,sample_data.column_b)
plt.plot(sample_data.column_a,sample_data.column_c)
plt.show()


#Ex 3: Data Visualisation (pt2)

#a) import data

import pandas as pd

data = pd.read_csv("countries.csv")
print(data)

#b) Compare population growth China vs US

us = data[data.country == "United States"]
cn = data[data.country == "China"]

plt.plot(us.year,us.population / 10**6)
plt.plot(cn.year,cn.population / 10**6)
plt.title("US & China Population")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend(["US","CN"])

plt.show()

