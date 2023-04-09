'''
This code was created as my matplotlib tutorial which can be found at https://aeryck.com/post:5
'''
import random
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
data = random.sample(range(100), 10)
print(data)
ax.plot(data)

plt.show()

data1 = random.sample(range(100), 5)
data2 = random.sample(range(100), 5)
print(f'data1: {data1}, data2: {data2}')
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(data1)
ax2.plot(data2)
plt.show()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(data1)
ax1.plot(data2)
bar_labels = ['1', '2', '3', '4', '5']
ax2.bar(bar_labels, data1)
ax3.scatter(data1, data2)
plt.show()
