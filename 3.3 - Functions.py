############### 3.3 Functions #############

print (dir()) # this will show all the list, dictionary or functions in memory


############### Basic Functions #############

#1) Pass Function
def f():
    pass #skip this line

print(f())

#2) Return Function
def ping():
    return "Ping!" #return ask function to return something

print(ping())

#3) Assign function to variable

x = ping()

print(x)

print (dir())


############### Interm. Functions #############

#1) Function for volume of Sphere

import math
print(dir(math))

print(math.pi)

def Volume(r):
    v = (4.0/3.0) * math.pi * r**3
    return v

print(Volume(10))

#2) Function for Air Triangle

#Volume of Triange ==> A = (0.5) * b * h

import math

def Triangle_Area(b,h):
    A = (0.5) * b * h
    return A

print(Triangle_Area(2,5))

#3) Convert to CM

#Converts a lenth from feet and inches to centimeters

import math

def cm(feet = 0,inches =0):
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 2.54 * 12
    return inches_to_cm + feet_to_cm

print(cm(feet = 5))
print(cm(feet = 5, inches= 8))

#4) BMI

#Converts a lenth from feet and inches to centimeters

import math

def BMI_calc(name,height_m,weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

#BMI Stats

name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK Sis"
height_m2 = 1.8
weight_kg2 = 70

name2 = "YK Bro"
height_m2 = 2.5
weight_kg2 = 160

result1 = BMI_calc(name1, height_m1, weight_kg1)

print(result1)

#5) List - Sorting Function

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second
print(full)

full.sort() #other way to sort

print(full)

print(dir(list())) #print directory of lists

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)
print(full_sorted)

#6) List - Upper Function

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

#6) List - Index Function

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

#67) Importing Packages

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Import radians function of math package
from math import radians

# Definition of radius
r = 192500
phi = radians(12)

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * phi

# Print out dist
print(dist)
