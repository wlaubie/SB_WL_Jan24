###########Functions

######User defined functions

#ex 1: Basics

#Basic function
def Helloworld():
    return print("Hello World")

print(Helloworld())

#Print function
def Add(x,y):
    print(x+y)

print(Add(5,7))


#Return function > we use return function when we want to link it to a variable
def returnAdd(x,y):
    """run function""" #this allows to describe function
    return (x+y) #function finishes at return
    print("hello") #this won't run

sum = returnAdd(10,65) # works as linked to return function
test2 = Add(4,8) # can't link to a variable as no return function

print(sum) #works
print(test2) #fails


#2: Unpacking Tuples

even_nums = (2,4,6)

a,b,c = even_nums #link to tuple above

print(a)
print(b)
print(c)


#3: Functions & Tuples

def raise_both(value1,value2):
    """raise value 1 to power of value 2 and vice versa"""
    new_value1 = (value1 ** value2)
    new_value2 = (value2 ** value1)
    new_tuple = (new_value1, new_value2)
    return new_tuple

result = raise_both(2,3)

print((result))

#3: Functions & Tuples (part 2)

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    """Return a tuple of strings"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'

    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'

    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words


# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you') #assign congrats to yell1 and you to yell2

# Print yell1 and yell2
print(yell1)
print(yell2)


#4: Dicitonary and looping

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
##df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
##col = df['lang']
##print(col)

# Iterate over lang column in DataFrame
##for entry in col:

    # If the language is in langs_count, add 1
##    if entry in langs_count.keys():
##        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
##    else:
##        langs_count[entry] = 1

# Print the populated dictionary
##print(langs_count)

#5: Loops as function

# Define count_entries()
##def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Extract column from DataFrame: col
##    col = df[col_name]

    # Iterate over lang column in DataFrame
##    for entry in col:

        # If the language is in langs_count, add 1
##        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
##        else:
##            langs_count[entry] = 1

    # Return the langs_count dictionary
##    return langs_count


# Call count_entries(): result
##result = count_entries(tweets_df, 'lang')

# Print the result
##print(result)