###########Ierators

######Iterators

#ex 1: Iterators - Basics

users = ["John", "Paul", "Elliot", "Bobby","Sarah"]

for user in users:
    print(user)

print("-"*20)

looper = iter(users)
while True:
    try:
        user = next(looper)
        print(user)
    except StopIteration:
        break

######Zip

#ex 1: Zip - Basics

prices = [10000, 20000, 30000]
car_sizes = ["small", "large", "medium"]
colors = ["Red", "Blue"]

print(list(zip(prices,car_sizes)))

#ex 2: Zip - Unpack

for z1,z2 in zip(prices, car_sizes):
    print(z1,z2)

#or
z = zip(prices,car_sizes)

print(*z)

#ex 3: Zip & Dictionary

# Zip lists: zipped_lists
##zipped_lists = zip(feature_names,row_vals)

# Create a dictionary: rs_dict
##rs_dict = dict(zipped_lists)

# Print the dictionary
##print(rs_dict)


######Enumerate

#ex 1: Enumerate - Basic

avengers = ['paul','bryan','john','haul']
e = enumerate(avengers) #add index of each values
e_list = list(e)

print(e_list)

#ex 2: Enumerate - Unpack

for index,value in enumerate(avengers):
    print(index,value)

#or

for index,value in enumerate(avengers, start = 10):  #assign starting index at 10
    print(index,value)



