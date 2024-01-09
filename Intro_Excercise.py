#######Spring Board - Python Refresher

###############Beginner Training

#1) Code to Enter Age
#birth_year = input("Enter your birth year: ")
#age = 2023 - int(birth_year)
#print(age)

#2) Capital Letters
course = "Python for Beginners"

print(course.upper())

#3) Find where letter of string is located
print(course.find("y"))

#4) Replace in String
print(course.replace("for","5"))

#5) Boolean Expression
price = 25
print(price > 10 and price < 30)
#Will return "True"


###############IF CONDITION

#1) If Expression

Temperature = 25
if Temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif Temperature >20: #(> 20, < 30)
    print("It's a nice day")
print("Done")

#2) Excercise: Weights

#Weight = input("Enter your Weight: ")
#Measure = input("Enter your Measure: ")


#if Measure == "l":
#    Result = (int(Weight) / 2.20462)
#elif Measure == "k":
#    Result = (int(Weight) * 2.20462)
#print(Result)


###############WHILE CONDITION

#1) While Condition


i = 1

while i <= 5:
    print(i)
    i = i + 1

#2) While Condition with strings

i = 1

while i <= 5:
    print(i*"*")
    i = i + 1

###############Lists

#1) Intro to Lists
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)
print(names[1])       #to pick a name in list
print(names[-1])       #to pick a name in list

names[0] = "Jon" #repalcing John in list with Jon
print(names)

print(names[0:3]) #print first 3 names



#2) List APPEND

numbers = [1, 2, 3, 4, 5]
numbers.append(6) #add number to end
print(numbers)

#3) List Insert

numbers = [1, 2, 3, 4, 5]
numbers.insert(0,-1) #insert number (location, value to add); [-1] locates last value
print(numbers)

#4) List Remove / Pop

numbers = [1, 2, 3, 4, 5]
numbers.remove(3) #remove value from list
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.pop() #remove last list value
print(numbers)

#5) inverse "ban" with "micro"
lis = ["ban", "apl", "micro"]
lis.pop()
lis.remove("ban")
lis.insert(0,"micro")
lis.append("ban")
print(lis)

#or
lis = ["ban", "apl", "micro"]
temp = lis[0]
lis[0] = lis[2]
lis[2] = temp
print(lis)

#or
lis = ["ban", "apl", "micro"]
lis[0], lis[2] = lis[2], lis[0]
print(lis)

#6) Clear Remove

numbers = [1, 2, 3, 4, 5]
numbers.clear() #clear list
print(numbers)

#7) Item exist in list?

numbers = [1, 2, 3, 4, 5]
print(1 in numbers) #will reply True

#8) How many items in list

numbers = [1, 2, 3, 4, 5]
print(len(numbers))


###############For Loop

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i+1


###############Range Function

#1)
numbers = range(5) #includes numbers from 0 to 4 (excludes 5)

print(numbers)

for i in numbers:
    print(i)

#2)
numbers = range(5,10) #includes numbers from 5 to 9 (excludes 10)

print(numbers)

for i in numbers:
    print(i)

#3)

numbers = range(5,10,2) #includes numbers from 5 to 9 by jump of 2

print(numbers)

for i in numbers:
    print(i)



for i in range(5):
    print(i)


###############Tuples (same as list but immutable - cant be changed)

#Lists = []
#Tuples = ()