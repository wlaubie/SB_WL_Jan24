###### 5.1 - MatplotLib


#Ex 1: Plotting

import matplotlib.pyplot as plt
#matplotlib.use('Qt5Agg')
#print(plt.__version__)


x = list(range(0,10))
y = list(range(-10,0))

plt.plot(x,y)  #plot x,y
plt.show()           #show the graph


#Ex 2: Plotting

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis((0, 6, 0, 20))
plt.show()

#Ex 3: Plotting

import matplotlib.pyplot as plt

a = [0,-100,25,67,-323] #X Axis
b = [0,3,7,3,9]         #Y Axis
plt.plot(a,b)
plt.show()

#Ex 3: Zoom in on the triangle

plt.axis([-50,80,2,8]) #Allows to redefine the X axis which will allow you to capture a specific portion of results
plt.plot(a,b)
plt.show()


#Ex 3: Graph Title, Axis Label

a = [0,-100,25,67,-323] #X Axis
b = [0,3,7,3,9]         #Y Axis

plt.title("Triangle")
plt.xlabel("Array A")
plt.ylabel("Array B")

plt.axis([-50,80,2,8])
plt.plot(a,b)
plt.show()

#Ex 4: Override X lables with different labels names

a = [0,-100,25,67,-323] #X Axis
b = [0,3,7,3,9]         #Y Axis

plt.title("Triangle")
plt.xlabel("Array A")
plt.ylabel("Array B")

plt.axis([-50,80,2,8])
plt.xticks((-40,-20,0,20,40,60,80),("h","e","l","l","o","o","o")) #override here

plt.plot(a,b)
plt.show()

#Ex 5: Change color of graph

a = [0,-100,25,67,-323] #X Axis
b = [0,3,7,3,9]         #Y Axis

plt.title("Triangle")
plt.xlabel("Array A")
plt.ylabel("Array B")

plt.axis([-50,80,2,8])

plt.plot(a,b, color = "red") #make it red
plt.show()


#Ex 6: Histogram

a = [0,-100,25,67,-323] #X Axis
b = [0,3,7,3,9]         #Y Axis


plt.hist(a)
plt.show()

#Ex 7: Scatter

a = [0,-100,25,67,-323] #X Axis
b = [0,3,7,3,9]         #Y Axis


plt.scatter(a,b)
plt.show()


#Ex 7: Convert Axis to Logarithmic scale


a = [0,-100,25,67,-323] #X Axis
b = [0,3,7,3,9]         #Y Axis

plt.xscale("log")
plt.scatter(a,b)
plt.show()

#Ex 8: Histogram

values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins=3) #will devise the data in 3 bins
plt.show()
plt.clf() #cleans up histo to mae a new one behind

values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins=6) #will devise the data in 6 bins
plt.show()
plt.close()

#Ex 8: Graph Customization

import matplotlib.pyplot as plt

year = [1950, 1951, 1952, 2100]
pop = [2.53, 2.57, 2.62, 10.85]

plt.plot(year, pop)

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population")
plt.yticks([0,2,4,6,8,10],["0","2b","4b","6b","8b","10b"])

plt.show()

#Ex 9: Add xaxi and y axis inputs to graph

import matplotlib.pyplot as plt

year = [1950, 1951, 1952, 2100]
pop = [2.53, 2.57, 2.62, 10.85]

year = [1800, 1850, 1900] + year
pop = [1.0,1.262, 1.650] + pop

plt.plot(year, pop)

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population")
plt.yticks([0,2,4,6,8,10],["0","2b","4b","6b","8b","10b"])

plt.show()

#Ex 10: Things to add to the bubble plot of each country gdp vs life exp.

# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
# x = x axis
# y = y axis
# s = size of bubble for each country
# c = colours for each continent
# alpha = range from 0 to 1 (make the colours transparant)


#Ex 11: Scatter Plot

# Scatter plot
#plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India') #will add custom texts in graph at location
plt.text(5700, 80, 'China')#will add custom texts in graph at location

# Add grid() call
plt.grid(True) #will add grid lines

# Show the plot
plt.show()

