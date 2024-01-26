###########Loop

#ex 1: For Loop of range

total = 0

for x in range(1,5):
    print(x)
    total = total + x

print(total)

#other quicker way of writting this is:

total = 0

for x in range(1,5):
    print(x)
    total += x                              #quick easy print

print(total)

#ex 2: While Loop

total1 = 0
j = 1

while j < 5:
    print(j)
    total1 += j
    j += 1

print(j) #exit condition when reached 5
print(total) #total


#ex 3: While Loop on ordered listo f numbers


given_list = [5,4,4,3,1,-2,-3,-5]
total2 = 0
i = 0

while given_list[i] > 0:
    total2 += given_list[i]
    i += 1

print(i) #exit condition when reached 5
print(total2) #total

#ex 3: For Loop on ordered listo f numbers


given_list2 = [5,4,4,3,1,-2,-3,-5]
total3 = 0


for element in given_list2:
    if element <= 0:
        break               #exit for loop and while loops
    total3 += element

print(total3)
