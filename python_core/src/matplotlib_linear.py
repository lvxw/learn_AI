import matplotlib.pyplot as plt

a = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
b = list(map(lambda x: x*x, a))

plt.plot(a, b)
plt.title('line chart')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

