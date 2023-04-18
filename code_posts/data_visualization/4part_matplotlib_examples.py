# exercise 1
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(101)

fig, ax = plt.subplots()
COLOR_BLUE = '#1F77B4'
COLOR_ORANGE = '#FF7F0E'
COLOR_GREEN = '#2CA02C'
COLOR_PURPLE = '#9467BD'

'''
# exercise 1
data1 = rng.random((2, 100))
data2 = rng.random((2, 100))

ax.scatter(*data1, marker='*', label='data1') # *data1 = (data1[0], data1[1])
ax.scatter(*data2, marker='o', label='data2')

ax.set_title('Randomly generated data')
ax.legend()

plt.show()

# exercise 2
fig, ax = plt.subplots()
sizes = [25, 20, 45, 10]
labels = ['A', 'B', 'C', 'D']
explode = [0, 0, 0, 0.2]
colors = [COLOR_BLUE, COLOR_ORANGE, COLOR_GREEN, COLOR_PURPLE]

ax.pie(sizes, explode=explode, labels=labels, colors=colors)

plt.show()

# exercise 3
fig, axs = plt.subplots(2, 2, tight_layout=True)
line_data = rng.random((10,))
scatter_data = rng.random((2, 10))
bar_data = rng.random((3,))
bar_labels = ['A', 'B', 'C']
hist_data = rng.normal(0, 0.1, 100)


fig.suptitle('Four different plots of random data', weight='bold')
axs[0][0].set_title('Line plot')
axs[0][0].plot(line_data, color=COLOR_BLUE)
axs[0][1].set_title('Scatter plot')
axs[0][1].scatter(*scatter_data, color=COLOR_ORANGE)
axs[1][0].set_title('Bar plot')
axs[1][0].bar(bar_labels, bar_data, color=COLOR_GREEN)
axs[1][1].set_title('Histogram')
axs[1][1].hist(hist_data, color=COLOR_PURPLE)

plt.show()

# exercise 4
sales = rng.random((12,))
quarter_len = len(sales) // 4
quarters = [sales[i:i+quarter_len] for i in range(0, len(sales), quarter_len)]
quarter_avgs = [np.average(x) for x in quarters]
quarter_stds = [np.std(x) for x in quarters]
bar_labels = ['1st', '2nd', '3rd', '4th']

ax.bar(bar_labels, quarter_avgs, color=COLOR_BLUE, label='Average Sales')
ax.errorbar(bar_labels, quarter_avgs, yerr=quarter_stds, fmt='o',
    color=COLOR_ORANGE, label='Standard Deviation')

ax.set_title('Made-up Comapny Sales')
ax.set_xlabel('Quarter')
ax.set_ylabel('Sales ($)')
ax.legend()

plt.show()

# exercise 5
sales = 1000 * rng.random((3,4))
quarters = ['1st', '2nd', '3rd', '4th']
labels = ['Widgets', 'Gadgets', 'Gizmos']
colors = [COLOR_BLUE, COLOR_ORANGE, COLOR_GREEN]
bottom = np.zeros(len(quarters))
for i, product in enumerate(sales):
    ax.bar(quarters, product, label=labels[i], color=colors[i], bottom=bottom)
    bottom += product

ax.set_title('Sales of three made up products')
ax.set_xlabel('Quarter')
ax.set_ylabel('Sales (units)')
ax.legend()

plt.show()

# exercise 6
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
data = [rng.random((3, 100)) for _ in range(3)]
markers = ['o', '^', 's']
colors = [COLOR_BLUE, COLOR_ORANGE, COLOR_GREEN]
for i, dataset in enumerate(data):
    ax.scatter(*dataset, label=f'Dataset {i}', color=colors[i],
    marker=markers[i])

ax.set_title('Three sets of random data')
ax.set_xlabel('x', fontweight='bold')
ax.set_ylabel('y', fontweight='bold')
ax.set_zlabel('z', fontweight='bold')
ax.legend()

plt.show()

# exercise 7
data = rng.random((10, 10))
heatmap = ax.imshow(data, cmap='cividis')

for r in range(data.shape[0]):
    for c in range(data.shape[1]):
        ax.text(c, r, np.round(data[r, c], 1), ha='center', va='center', color='white')

cbar = fig.colorbar(heatmap, ax=ax)
ax.set_title('Heatmap of random data')

plt.show()

# exercise 8
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.linspace(0, np.pi, num=100)
theta = np.pi * r
ax.plot(theta, r)

plt.show()

'''
# exercise 9
x_range = (-2*np.pi, 2*np.pi)

x = np.linspace(*x_range, 100)
ax.plot(x, np.sin(x), lw=3, label='Sine')
ax.plot(x, np.cos(x), lw=3, label='Cosine')

ax.set(xlim=[*x_range], ylim=[-1.1, 1.1])
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 4))

def format_func(value, tick_number):
    N = int(np.round(value * 4 / np.pi))
    if N == 0:
        return '0'
    elif N == 1:
        return r'$\pi$/4'
    elif N == -1:
        return r'-$\pi$/4'
    elif N == 2:
        return r'$\pi$/2'
    elif N == -2:
        return r'-$\pi$/2'
    else:
        return ''

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
ax.legend()

plt.show()

'''
# exercise 10
a = np.arange(100)
b = 2 * a + 1 + rng.normal(scale=20, size=100)
ax.scatter(a, b, color=COLOR_BLUE, label='Random data')

# linalg.lstsq solution ======================================================
# linalg.lstsq performs linear regression by finding the closest solution to
# a @ x = b, where x will be a vector containing our least-squares solution.
# because we need x to be a 100x1 vector, we need to convert a to a nx100
# matrix
A = np.vstack([a, np.ones(len(a))]).T
result = np.linalg.lstsq(A, b, rcond=None)
m, c = result[0]
line_of_best_fit = [m*x + c for x in a]

SSR = result[1]
SST = sum((b - np.mean(b))**2)
R2 = 1 - (SSR / SST)

ax.plot(a, a*m+c, color=COLOR_ORANGE, lw=4, label='Best fit')
ax.set_title('Scatterplot with line of best fit')
ax.text(85, -40, f'$R^2$: {R2[0]:.3f}', fontweight='bold')
ax.legend()

plt.show()

# Polynomial.fit solution ====================================================
line, full = np.polynomial.polynomial.Polynomial.fit(a, b, deg=1, full=True)
c, m = line.convert()

SSR = full[0]
SST = sum((b - np.mean(a))**2)
R2 = 1 - (SSR / SST)

ax.plot(a, m*a+c, color=COLOR_ORANGE, lw=4, label='Best fit')
ax.set_title('Scatterplot with line of best fit')
ax.text(85, -40, f'$R^2$: {R2[0]:.3f}', fontweight='bold')
ax.legend()

plt.show()
'''
