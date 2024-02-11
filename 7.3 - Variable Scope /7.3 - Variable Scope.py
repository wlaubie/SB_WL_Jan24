###########Variable Scope

######Scope

#Not all objects are accessible everywhere in a script
#Scope - part of the program where an object or name may be accessible

#ex 1: Basics

# Create a string: team
team = "teen titans"


# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice League"


# Print team > no changes
print(team)

# Call change_team() > after calling function this gets updated to team
change_team()

# Print team > print new team wit updated global variable
print(team)


#ex 2: Nonlocal > allows to override values within functions (like global but within functions)

# Define change_team()
def outer():
    """Print the value of n."""
    n = 1

    def inner():
        nonlocal n
        n = 2
        print(n)

    inner()
    print(n)

outer()

#ex 3: Nested Function

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))


#ex 4: Nested Function with closure

# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

#ex 5: Nested Function with closure (pt2)

# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""

    # Concatenate word with itself: echo_word
    echo_word = word * 2

    # Print echo_word
    print(echo_word)

    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""
        # Use echo_word in nonlocal scope
        nonlocal echo_word

        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'

    # Call function shout()
    shout()

    # Print echo_word
    print(echo_word)


# Call function echo_shout() with argument 'hello'
echo_shout('hello')



######Default Arguments

#1: Default Argument

def power(number, pow =1):
    """Raise number to the power of pow."""

    new_value = number ** pow
    return new_value

#power: 2 arguments
print(power(9,2))

#power: 2 arguments
print(power(9,1))

#power: 1 arguments >> will used default power of 1
print(power(9))


#2: *Args - Flexible arguments

#used when not sure how many arguments you will be using. Can input multiple arguments un function

def add_all(*args):       #*args allows to put all arguments and transform them in a tuple
    """Sum all values in *args together"""

    #Initialize sum
    sum_all = 0

    # Accumulate the sum
    for num in args:
        sum_all += num
    return sum_all

#3: **kwargs - Flexible arguments

#used for flexible decitionary keys and values

def print_all(**kwargs):       #*8kwargs converts all into a dictionary
    """Print out key-value pairs in **kwargs"""

    # Print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)

print_all(name="dumbledore", job="headmaster")


#4: Default Argument - Practice

# Define shout_echo
def shout_echo(word1, echo = 1, intense = False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey', echo = 5, intense = True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo('Hey', intense = True)

# Print values
print(with_big_echo)
print(big_no_echo)

#5: *args - Practice

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ''

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish('luke')

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)


#6: **kwargs - Practice

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, values in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + values)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi",status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")


#7: Bringing it all together

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count


# Call count_entries(): result1
##result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
##result2 = count_entries(tweets_df, 'source')

# Print result1 and result2
##print(result1)
##print(result2)