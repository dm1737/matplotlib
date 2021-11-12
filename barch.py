import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

# Create colored bar charts
plt.bar(x,y, label='Bars1', color='black')
plt.bar(x2,y2, label='Bars2', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph')
plt.legend()
plt.show()