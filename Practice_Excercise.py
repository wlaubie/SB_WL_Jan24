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

