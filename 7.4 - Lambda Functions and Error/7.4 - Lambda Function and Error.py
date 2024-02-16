###########Lambda Functions & Errors

######Lambda Functions & Anonymous functions

#ex 1: Lambda function

#regular function
def f(x):
    return 3*x + 1

print(f(2))

#Lambda function
g = lambda x: 3*x +1
print(g(2))


#ex 2: Lambda 2 variables

full_name = lambda  fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("     leonard", "EULER"))


#ex 3: Lambda & Quadratic function

def build_quadratic_function(a,b,c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2,3,-5)

print(f(0))
print(f(1))

#other way to write it

print(build_quadratic_function(3,0,1)(2)) #3x^2 + 1

######Maps

#1: Basics - Map

import math

def area(r):
    """area of a circle with readius 'r' """
    return math.pi * (r)**2

radii = [2,5,7.1,0.3,10]

#Method 1: Direct Method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

#Method 2: use "map" function

print(map(area,radii)) #map(function, list/tuple/collection of data to run in function)
print(list(map(area,radii)))

######Filter

import statistics

#1: Basics - Filter

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg = statistics.mean(data)
print(avg)

k = list(filter(lambda x: x > avg, data)) #filter data for values > avg

print(k)

#2: Filter - filtering out empty valurs in list

countries = ["", "Argentina", "", "Brazil", "", "Chile", "", "Colombia", ""]

f = list(filter(None, countries)) #filters our empty values
print(f)

#3: Filter on file for tweets

# Select retweets from the Twitter DataFrame: result
##result = filter(lambda x: x[0:2] == "RT",tweets_df['text'] )

# Create list from filter object result: res_list
##res_list = list(result)

# Print all retweets in res_list
##for tweet in res_list:
##    print(tweet)

######Dealing with Error for functions

try:                        #try executing portion in try if not it moves to Except
    pass
except FileNotFoundError:    #if fails try will read except, but if no error in try, it will skip except
    pass
except Exception:           #Excetption is the most general exception type
    pass
else:                       #will run after try / except
    pass
finally:                    #will no matter what
    pass

#Ex1: Try + Except

#Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ""
    shout_words = ""

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + "!!!"
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")


#Ex2: Raise + Try + Except

def sqrt(x):
    if x < 0:
        raise ValueError('x must be non-negative')
    try:
        return x ** 0.5
    except TypeError:
        print("x must be an int or float")

print(sqrt(4))
print(sqrt("i"))
print(sqrt(-3))