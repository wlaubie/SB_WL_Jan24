###########Random and Random Walks


######Random


#ex 1: Random numbers

# Display 10 random numbers from interval [0,1)

import random
print(dir(random))

for i in range(10):
    print(random.random()) #uniform distribution - every value equallyl likely to occur

#ex 2: Function with Random numbers

# Display 10 random numbers from interval [0,1)

import random

def myrandom():
    #random, scale, shift, return
    return  4*random.random() + 3


for i in range(10):
    print(myrandom()) #uniform distribution - every value equallyl likely to occur


#ex 3: Uniform function

# Display 10 random numbers from interval [0,1)

import random

for i in range(10):
    print(random.uniform(3,7)) #pick 10 random numbers between 3 and 7


#ex 4: Bell Curve
# Display 10 random numbers from interval [0,1)

import random

for i in range(20):
    print(random.normalvariate(0,1)) #normal distribution with mean 0 and stdv 1

#Numbers bumched around 0. If stdv high, wider if stdv smaller is tighter to mean

#ex 6: Random from list (rock, paper, scisor)

import random

for i in range(20):
    print(random.randint(1,6)) #random integers between 1 and 6

#ex 5: Roll a dice random integer

import random

outcomes = ["rock", "paper", "scissors"]

for i in range(20):
    print(random.choice(outcomes)) #random integers between 1 and 6


######Random Walk


#ex 1: Random walk

import random

def random_walk(n):
    #returns coordinates after "n" blocks random walk

    x = 0
    y = 0
    for i in range(n):
        step = random.choice(["N","S","E","W"])
        if step == "N":
            y = y + 1
        elif step == "S":
            y = y - 1
        elif step == "E":
            x = x + 1
        else:
            x = x - 1
    return (x,y)

for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ",
                 abs(walk[0] + abs(walk[1]))) #returns x,y

#ex 2: Random walk - shorter version

import random

def random_walk(n):
    #returns coordinates after "n" blocks random walk

    x, y = 0, 0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)


for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ",
                 abs(walk[0] + abs(walk[1]))) #returns x,y


#ex 3: Random walk - Montecarlo simulation

import random

def random_walk_2(n):
    #returns coordinates after "n" blocks random walk

    x, y = 0, 0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)

number_of_walks = 1000 #change it to 20k to check real simulation

for walk_length in range (1,31):
    no_transport = 0 #number of walks 4 or fewer blocks

    for i in range(number_of_walks):
        (x,y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, "/ % of no transport = ", 100*no_transport_percentage )




#### Random using Numpy

#1: Random with Numpy

# Import numpy as np
import numpy as np

# Set the seed: makes the random number always the same (so random but not so much - used when conducting analysis)
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

#2: Dice Roll

import numpy as np

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5:
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step)


#3: Random Walk with Dice throw

import numpy as np

np.random.seed(123)
tails = [0]

for x in range(10):
    coin = np.random.randint(0,2)
    tails.append(tails[x] + coin)

print(tails)


#4: Random Walk with Dice throw + Graph

import numpy as np

# NumPy is imported, seed is set
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = max(step - 1,0)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Graph random_walk
import matplotlib.pyplot as plt

plt.plot(random_walk)
plt.show()



#5: Random Coin Toss + Histograam

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
final_tails = []

for x in range(10000):
    tails =[0]

    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])

plt.hist(final_tails,bins = 100)
plt.show()


#6: Random Coin Toss + Histograam

import numpy as np
import matplotlib.pyplot as plt

# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()