###########Logic, Control Flow and Filtering


###########Logic Operations


#Data Frame

#Ex1: Data Frame Logic operations
#Objectives: select countries with area over 8m km2
#3 steps:
#a) select area column
#b) do comparison on area column
#c) use resilt to select countries


import pandas as pd

brics = pd.read_csv("brics.csv", index_col= 0)
print(brics)

print(brics["area"]> 8)

is_huge = brics["area"] > 8

print(brics[is_huge]) #give result of what we want for condition we want


#Ex2: Further Advancment

import numpy as np

filter = np.logical_and(brics["area"] > 8, brics["area"] < 10)
print(brics[filter]) #filter array within data frame


#Ex3: While Loop

#Create the variable offset with an initial value of 8.
#Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
#Print out the sentence "correcting...".
#Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
#Finally, still within your loop, print out offset so you can see how it changes.

# Initialize offset
offset = 8

# Code the while loop

while offset !=0:
    print("correcting...")
    offset = offset - 1
    print(offset)

# Ex3: For Loop - basic

# Initialize offset
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)

# Code the For loop

for x in fam:                       #for each element x in fam (total of 4 elements look for below)
    print(x)                        #print x


# Ex4: For Loop - enumerate

# Initialize offset
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)

# Code the For loop

for index, x in enumerate(fam):                                        #for each element x in fam we use enumerate to add Index
    print("index" + str(index) + ": " + str(x))                        #print x wtih Index


# Ex5: Loop over String

# Initialize offset
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)

# Code the For loop

for c in "family":
    print(c.capitalize())

# Ex6: For Loop with 2 variables

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for x, y in house:
    print("the " + str(x) + " is " + str(y) + " sqm")


# Ex7: For Loop over dictionaries

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe

for key, value in europe.items():                           #key, value
    print("the capital of " + key + " is " + str(value))    #print key, value


# Ex8: For Loop over Arrays

# Import numpy as np
import numpy as np

# For loop over np_height (1d array)
#for x in np_height:
#    print(str(x) + " inches")

# For loop over np_baseball (2d array)
#for x in np.nditer(np_baseball):
#    print(x)


# Ex9: For Loop over DF

# Import pandas library
import pandas as pd

brics = pd.read_csv("brics.csv", index_col = 0)

# For loop over brics
for lab, row in brics.iterrows():               #us iterrows to retieve data for rows and columns
    print(lab)
    print(row)

# Ex10: For Loop over DF wtih targeted row

# Import pandas library
import pandas as pd

brics = pd.read_csv("brics.csv", index_col = 0)

# For loop over brics
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])

# Ex11: For Loop to create new column

# Import pandas library
import pandas as pd

brics = pd.read_csv("brics.csv", index_col = 0)

# For loop over brics
for lab, row in brics.iterrows():
    #create series on every iteration
    brics.loc[lab,"name_length"] = len(row["country"])
print(brics)

#or

brics["name_length"] = brics["country"].apply(len)
print(brics)


# Ex12: For Loop to create new column with Capital letters

# Import cars data
import pandas as pd
brics = pd.read_csv('brics.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in brics.iterrows():
    brics.loc[lab, "COUNTRY"] = row["country"].upper()


# Print brics
print(brics)

#or

brics["COUNTRY"] = brics["country"].apply(str.upper)
print(brics)
