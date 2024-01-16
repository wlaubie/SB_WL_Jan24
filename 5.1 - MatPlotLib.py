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