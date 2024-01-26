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

number_of_walks = 20000

for walk_length in range (1,31):
    no_transport = 0 #number of walks 4 or fewer blocks

    for i in range(number_of_walks):
        (x,y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, "/ % of no transport = ", 100*no_transport_percentage )
