import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,110,12,35,96,130,123,44,22,10,48,43,57,86,49,32]

# partitions for data into bars
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

# create histogram, with bin delimeters, bar type, and adjusted width
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph')
plt.legend()
plt.show()