import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

# Plot x and y values, label creates legend
plt.plot(x,y, label='Line 1')
plt.plot(x2,y2, label='Line 2')

# Assign names to x and y axes
plt.xlabel('Plot Number')
plt.ylabel('Important var')

# Display graph with title and legend
plt.title('Graph\nCheck it')
plt.legend()
plt.show()