import matplotlib.pyplot as plt

plt.ion()

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

plt.plot(x1, y1, label="Line 1")
plt.scatter(x1, y1)

plt.plot(x2, y2, label="Line 2")


plt.title("Simple Visualization Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.legend()

plt.pause(0.001)
plt.show()