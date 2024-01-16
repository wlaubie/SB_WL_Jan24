###### 3.4 - Numpy (numeric python)

import numpy as np
print(np.__version__)

#Ex 1: BMI calculation using Numpy arrays (from list)

Height = [1.73, 1.68, 1.71, 1.89, 1.79]
Weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(Height)
np_weight = np.array(Weight)

print(np_height)
print(np_weight)

bmi = np_weight / (np_height)**2
li = list(bmi) #converting back to list

print(bmi)

print(li)

#Ex 2: Numpy Subsetting

print(bmi[1]) #get 1st element of array
print(bmi > 23) #will check every element of array and see if True or False
print(bmi[bmi > 23]) #return elements where bmi > 23


#Ex 2: NP Array Multiplication

#Ask
#Create a numpy array from height_in. Name this new array np_height_in.
#Print np_height_in.
#Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
#Print out np_height_m and check if the output makes sense.

# Import numpy
import numpy as np

height_in = (74,74,72,73,69)
weight_lb = (180, 215, 210, 176, 160)

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np.multiply(np_height_in,0.0254)

# Print np_height_m
print(np_height_m)

#Notes Array Nump

#Operations
#a) #add = np.add(list1, list2)
#b) #sub = np.subsrtract(list1, list2)
#c) #div = np.divide(list1, list2)
#d) #mult = np.multiply(list1, list2)
#e) #dot = np.dot(list1, list2)

#Notes State Function

#a) #sqrt = np.sqrt(25)
#b) #abs = np.abs(-2)
#c) #power = np.power(2, 7)
#d) #log = np.log(25)
#e) #exp = np.exp([2,3])
#f) #min = np.min(list1)
#g) #max = np.max(list2)
#h) #mean = np.mean(list2)
#i) #mdedian = np.median(list2)
#j) Correlation = np.corrcoef(np_city[:,0], np_city[:,1])
#k) STD = np.std(np_city[:,0])
#l) sum(), sort()

#Ex 3: NP Array BMI Calc

#Ask
#Create a numpy array from the weight_lb list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting numpy array as np_weight_kg.
#Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
#Print out bmi.

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592
print(np_weight_kg)

# Calculate the BMI: bmi
BMI = np.divide(np_weight_kg,np.power(np_height_m,2))


# Print out bmi
print(BMI)


#Ex 4: Boolean Numpy Array

#Ask
#Create a boolean numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
#Print the array light.
#Print out a numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.

# Import numpy
import numpy as np

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi > 5

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
#or
print(bmi[bmi > 5])




#Ex 5: 2D Numpy Arrays (explained)


np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],[65.4, 59.2, 63.6, 88.4, 68.7]])
print(np_2d)
print(np_2d.shape) #givei nfor on data structure, here resulst is (2,5) which is 2 rows, 5 columns (all matrices same size)

print(np_2d[0,2]) #rows / column
print(np_2d[:, 1:3]) #across all rows, pick elements 1:3 of columns
print(np_2d[1, :]) #get entire 2nd row

#Ex 6: Practice 2d Array

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
baseba = ([[74, 75, 72, 75],[190, 215, 210, 205]])
baseball = np.array(baseba)
print(baseball)

np_baseball = np.array(baseball)
print(np_baseball)

# Print out the 50th row of np_baseball
print(np_baseball[1:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]
print(np_weight_lb)

# Print out height of 124th player
print(np_baseball[1][0])



import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(np_mat * 2)
print(np_mat + np.array([10, 10]))
print(np_mat + np_mat)



#Ex 7: Practice 2d Array

print(np.array([0, True, "python"]))