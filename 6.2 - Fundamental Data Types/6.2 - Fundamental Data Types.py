##### 6.2 - Fundamental Data Types

###Tuples

#1: List and Tuples

#List example
prime_numbers = [2,3,5,7,11,13,17]

#Tuples example: ordered list
perfect_sqaure = (1,4,9,16,25,36)

#Display lenghts
print("# Primes = ", len(prime_numbers))
print("# Primes = ", len(perfect_sqaure))

print("list methods")
print(dir(prime_numbers)) #check items after subclasshook
print(80*"-")
print("Tuple methods")
print(dir(perfect_sqaure)) #check items after subclasshook >> less available for Tuples

#Difference between the 2:
#List: add, remove, change data
#Tuples: cannot be changed or immutable

#Ex:2 : create Tuples with or without parenthesis

test1 = 1, #need to add a coma to make it a tuples
test2 = 1,2
test3 = 1,2,3

print(test1)
print(test2)
print(test3)

print(type(test1))
print(type(test2))
print(type(test3))

#Ex3: Tuples application

#(age, country, knows_python)

survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2

print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)


###Sets

#Ex1: Basics

example = set()
print(dir(example))

print(help(example.add))

#Add function: can add elements of different type to the set
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)

example.add(42) #set do no contain duplicate elements
print((example))

#Remove function: remove element of set
example.remove(42)
print((example))

#Discard function: remove element of set if it is a member

example.discard(50) #50 not an element of set but no error

#Ex 2: Building/deleting Sets

example2 = set([28, True, 2.71828, "Helium"])
print(example2)

#Delete all elements of set
example2.clear()

print((example2))

#Ex 3: Union and Intrersection of Set

odds = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10])

#Sets Union
odds.union(evens)
print(odds.union(evens))

#Note both odds and evens remain unchanged
print(odds)
print((evens))

#Sets Intersection

odds.intersection(primes)
print(odds.intersection(primes))

##Practice Excercise

#Ex1: Practice

# Create a list containing the names: baby_names
baby_names = ["Ximena", "Aliza","Ayden", "Calvin"]

# Extend baby_names with 'Rowen' and 'Sandeep'

baby_names.extend(["Rowen", "Sandeep"])
print(baby_names)

# Find the position of 'Rowen': position
position = baby_names.index("Rowen")
print(position)

# Remove 'Rowen' from baby_names (using position)
baby_names.pop(4) #using position

# Print baby_names
print(baby_names)

#Ex2: Applying List Comprehesion to loop through a list of list

# Create the list comprehension: baby_names
##baby_names = [item[3] for item in records] #this will go through every item in records and pick up item[3]

# Print the sorted the names in alphabetical order
##print(sorted(baby_names)) #sort out pulled out list

#Ex6: Zip

#Zip 2 lists

# list1 = us_cookie
# list2 = in_cookie

#top_pairs = list(zip(list1,list2))


#Ex3: Enumerate (returns position of data in loop)

#Loop with Enumerate
#for idx, item in enumerate(top_pairs):
#    us_cookies, in_cookies = item
#    print(idx,us_cookie,in_cookie)

#Ex8: Enumerate practice (returns position of data in loop)

# Pair up the girl and boy names: pairs
##pairs = zip(girl_names, boy_names)

# Iterate over pairs
##for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
##    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
##    print(f'Rank {rank+1}: {girl_name} and {boy_name}')


###Strings

#1: f-strings

cookie_name = "Anzac"
cookie_price = "$1.99"

print(f"Each {cookie_name} cookie costs {cookie_price}.") #write a sentence with f-strings and variables

#2: String join method "".join()

child_ages = ["3", "4", "7", "8"]
print(", ".join(child_ages)) #this will print all chile_ages and split it with ", "

print(f"The children are ages {','.join(child_ages[0:3]) }, and {child_ages[-1]}.")

#3: String: .startswith() and .endswith()

boy_names = ["Mohamed", "Youssef", "Ahmed"]

print([name for name in boy_names if name.startswith("A")]) #will iterate through the Tuple and retrieve string staring with "A"

#3: String: searchin string

print("long" in "Life is a long lesson in humility")

print("life" in "Life is a long lessin in humility") #false as search is case sensitive

print("life" in "Life is a long lessin in humility".lower()) #lower makes all string in low cap

#4: Practice: unpacking Tuples

##for top_ten_rank, name in top_ten_girl_names:
  	# Print each name in the proper format
    ##print(f"Rank #: {top_ten_rank} - { name }")


#5: Practice: unpacking Tuples

# The top ten boy names are:  as preamble
##preamble = "The top ten boy names are: "

# , and as conjunction
##conjunction = ", and"

# Combines the first 9 names in boy_names with a comma and space as first_nine_names
##first_nine_names = ", ".join(boy_names[0:9])

# Print f-string preamble, first_nine_names, conjunction, the final item in boy_names and a period
##print(first_nine_names)
##print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.")

#6: Practice: unpacking Tuples

# Store a list of girl_names that start with s: names_with_s
##names_with_s = [name for name in girl_names if name.lower().startswith('s')]

##print(names_with_s)

# Store a list of girl_names that contain angel: names_with_angel
##names_with_angel = [name for name in girl_names if 'angel' in name.lower()]

##print(names_with_angel)

