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






