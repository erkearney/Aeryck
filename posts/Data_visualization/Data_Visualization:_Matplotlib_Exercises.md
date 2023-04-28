We now have a solid understanding of how to use matplotlib to create fully
customizable plots. I've put together a series of exercises to help test your
understanding. With each question, I've added a sample Figure displaying a
correct solution, as well as one or more hints to help guide you. Good luck!

Please note, that not all the answers to these questions can be found within
this tutorial, that's because this tutorial was never meant to exhaustively
cover everything matplotlib, rather it was intended to provide foundational
skills. To solve these questions, you'll likely need to use the [matplotlib
official reference](https://matplotlib.org/stable/api/index).

## matplotlib series:
### [Basic plotting](https://aeryck.com/post:5)
### [Customization](https://aeryck.com/post:6)
### [The matplotlib API](https://aeryck.com/post:7)
### [Exercises (this post)](https://aeryck.com/post:8)

All the code from this post can be found
[here](https://github.com/erkearney/Aeryck/code_posts/data_visualization/4part_matplotlib_examples.py)

* * *
For brevity, assume these statements are included with every solution:

```python
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.deafult_rng(101) # not strictly necessary!

fig, ax = plt.subplots()

COLOR_BLUE = '#1F77B4'
COLOR_ORANGE = '#FF7F0E'
COLOR_GREEN = '#2CA02C'
COLOR_PURPLE = '#9467BD'
```

Many of these plots use randomly generated data, if you want your plots to look
like mine, you can set [the
seed](https://numpy.org/doc/stable/reference/random/generator.html) of the
random generator to 101 as I have done.

### Exercises 1-4 were selected to test your knowledge of basic plotting and customization with matplotlib.

1: Create a scatter plot using two datasets each consisting of 100 random data
points with values between 0 and 1. Use different marker styles and colors for
each dataset. Add a title and legend to the plot.
![Figure 1: Scatterplot of random data](static/images/data_visualization/matplotlib/exercises/1.png)
<details>
<summary>Hint(s)</summary>
1. You can use <a href="https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random">
numpy.random.Generator.random((2, 100))</a> to easily generated 100 random xy
datapoints. We've already created the Generator object above with

```python
rng = np.random.default_rng(101)
```

<br><br>

2. Check
<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html">Axes.scatter</a>
for help making a scatter plot.
</details>

<details>
<summary>Solution</summary>

```python
data1 = rng.random((2, 100))
data2 = rng.random((2, 100))

ax.scatter(*data1, marker='*', label='data1') # *data1 = (data1[0], data1[1])
ax.scatter(*data2, marker='o', label='data2')

ax.set_title('Randomly generated data')
ax.legend()

plt.show()
```

</details>

2: Create a pie chart with the following data: sizes = [25, 20, 45, 10]
and labels = ['A', 'B', 'C', 'D']. Customize the colors and explode the 'D'
slice.

![Figure 2: Pie chart with custom colors and exploded slice](static/images/data_visualization/matplotlib/exercises/2.png)
<details>
<summary>Hint(s)</summary>
This is simpler than it may seem, <a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html">
Axes.pie </a> already contains an 'explode' parameter. If you need a little more
explicit help, refer to <a
href="https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#explode-shade-and-rotate-slices">
this tutorial </a>.
</details>
<details>
<summary>Solution</summary>

```python
sizes = [25, 20, 45, 10]
labels = ['A', 'B', 'C', 'D']
explode = [0, 0, 0, 0.2]
colors = [COLOR_BLUE, COLOR_ORANGE, COLOR_GREEN, COLOR_PURPLE]

ax.pie(sizes, explode=explode, labels=labels, colors=colors)

plt.show()
```

</details>

3: Create a subplot with a 2x2 grid, displaying a line plot, scatter plot, bar
plot, and histogram using randomly generated data. Customize each plot with a
title and appropriate colors, and add a title to the Figure.

![Figure 3: Four different plots of random data](static/images/data_visualization/matplotlib/exercises/3.png)
<details>
<summary>Hint(s)</summary>
You will need to redefine the fig, ax = <a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots">
plt.subplots() </a> call.

<br>

<a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html">
Axes.plot </a><br>
<a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html">
Axes.scatter </a><br>
<a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html">
Axes.bar </a><br>
<a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html">
Axes.hist </a><br>
<a
href="https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random">
numpy.random.Generator.random </a><br>
You can use <a
href="https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal">
numpy.random.Generator.normal(0, 0.1, 100) </a> to generate a normal distribution for the histogram.
</details>
<details>
<summary>Solution</summary>
Remember to delete/comment fig, ax = plt.subplots()

```python
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
```

Remember to replace fig, axs = plt.subplots(2, 2) with fig, axs = plt.subplots() if you're going to do more exercises in the same file

</details>

4: Create a bar plot representing the average sales of a company across four
quarters in a year. Add error bars to show the standard deviation. Add a title,
labels, custom colors, and a legend.

![Figure 4: Made-up Company Sales, with Standard Deviation](static/images/data_visualization/matplotlib/exercises/4.png)
<details>
<summary>Hint(s)</summary>
You can use <a
href="https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random">
numpy.random.Generator.random </a> to generate the data, you could generate 12
data points, one for each month, 364 data points, one for each day, etc. However
you cannot simply generate one data point for each quarter, as then you won't
have enough data to calculate standard deviations.
<br>
<a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar">
Axes.bar </a>
<br>
<a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html">
Axes.errorbar </a>
</details>
<details>
<summary>Solution</summary>

```python
sales = rng.random((12,)) # 12 months in a year
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
```

</details>

### Exercises 5-8 were selected to test your ability to create 'non-standard' plots (i.e., plots that require a little more work than just calling Axes.plot_type.
5: Generate random data to simulate the sale of three products over four
quarters. Label the products as "Widgets", "Gadgets" and "Gizmos". Create a
stacked bar plot of this data, make each product a different color, and add a
title, legend, and axis labels.

![Figure 5: Stacked bar plot](static/images/data_visualization/matplotlib/exercises/5.png)

<details>
<summary>Hint(s)</summary>
You won't find an <i>Axes.stackedbar</i> method or anything at the sort, instead take a
close look at <a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html">
Axes.bar </a>.
<br><br>
Axes.bar has the <strong>bottom</strong> parameter, which is set to 0 by
default. What if we were to set the bottom according to previous data?
</details>
<details>
<summary>Solution</summary>

```python
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
```

</details>

6: Create a 3D scatter plot using three sets of random data points, each
containing 100 points with values between 0 and 1. Customize the plot by using a
different marker for each dataset, changing the colors, and adding a title and
legend.

![Figure 6: 3D scatterplot](static/images/data_visualization/matplotlib/exercises/6.png)
<details>
<summary>Hint(s)</summary>
You'll need to re-define the fig, ax = plt.subplots() call as follows:

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
```

<br>
Once you have a 3D subplot, you can simply call <a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter">
Axes.scatter</a> as before.
</details>
<details>
<summary>Solution</summary>

```python
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
```

</details>

7: Generate a 10x10 matrix with random values between 0 and 1. Use this data to
generate a heatmap. Change the color maps of the heatmap, and add text to each
cell of the heatmap to show its associated value, customize the color of the
text and center it both horizontally and vertically. Finally, add a colorbar and
a title.

![Figure 7: Colormap of random data](static/images/data_visualization/matplotlib/exercises/7.png)
##### (Colormap shown here: cividis)
<details>
<summary>Hint(s)</summary>
You won't find an <i>Axes.heatmap</i> method or anything of the sort. You'll
actually need to go digging around in the <i>image processing</i> section of the
documentation to solve this one.
<br><br>
The way computers process images are as matricies containing pixel values.
<br><br>
<a
href="https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html">
numpy.random.Generator.random</a><br>
<a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html">
Axes.imshow</a><br>
<a href="https://matplotlib.org/stable/api/colorbar_api.html">
matplotlib.colorbar</a>
</details>
<details>
<summary>Solution</summary>

```python
data = rng.random((10, 10))
heatmap = ax.imshow(data, cmap='cividis')

for r in range(data.shape[0]):
    for c in range(data.shape[1]):
        ax.text(c, r, np.round(data[r, c], 1), ha='center', va='center', color='white')

cbar = fig.colorbar(heatmap, ax=ax)
ax.set_title('Heatmap of random data')
```

</details>

### Exercises 8 and 9 are designed to test your knowledge beyond just matplotlib, specifically your ability to combine your plotting skills with your NumPy skills.
8: Plot an [Archimedean
spiral](https://en.wikipedia.org/wiki/Archimedean_spiral)

![Figure 8: Polar plot of Archimedean spiral](static/images/data_visualization/matplotlib/exercises/8.png)
</details>
<details>
<summary>Hint(s)</summary>
You will need to re-define the fig, ax = plt.subplots() call in a similar way to
exercise 5. Refer to the <a
href="https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure">
matplotlib.figure </a> section of the documentation.
<br><br>
Once you've converted the Figure to polar co-ordinates, you can actually use <a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html">
Axes.plot </a>. 
<br><br>
In a polar plot, the x-axis represents the angle (θ), and the y-axis represents
the distance (r) from the origin.
</details>
<details>
<summary>Solution</summary>

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.linspace(0, np.pi, num=100)
theta = np.pi * r
ax.plot(theta, r)

plt.show()
```

</details>

9: Generate 100 values of a linear function and 'corrupt' it with random
Gaussian noise. Plot these data as a scatterplot. Now using only matplotlib and
NumPy, perform a Linear Regression on the data and plot the result (i.e. plot a
line of best fit). Calculate the R^2 value of the regression. Add a title,
legend, and the R^2 value to the plot, and change the color and style of the
line representing the regression.
###### This problem is made easy using [seaborn](https://seaborn.pydata.org/generated/seaborn.regplot.html), which is why I've forbidden it from this exercise :). I do plan on eventually writing a seaborn tutorial.


You will find folks online suggesting
[numpy.polyfit](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html)
for a problem such as this, however, [the official numpy documentation
states](https://numpy.org/doc/stable/reference/routines.polynomials.html):
> ... the poly1d class and associated functions defined in numpy.lib.polynomial, such as **numpy.polyfit** and numpy.poly, are considered legacy and should not be used in new code.

So try to find a way to solve this problem without using it (free hint: the
[documentation
page](https://numpy.org/doc/stable/reference/routines.polynomials.html) I just linked to points to another method you can use!)


![Figure 9: Scatterplot of random data, with a line of best-fit added](static/images/data_visualization/matplotlib/exercises/9.png)

<details>
<summary>Hint(s)</summary>
1: To generate the initial data, you can write a linear function and use <a
href="https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal">
numpy.random.Generator.normal </a>. Then, just add the random data to the linear
function to 'corrupt' it.

<br><br>

2: You can either use <a
href="https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html">
numpy.linalg.lstsq </a> or <a
href="https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html#numpy.polynomial.polynomial.Polynomial.fit">
numpy.polynomial.polynomial.Polynomial.fit </a>. Of the two, the Polynomial
method is just a tad easier.

<br><br>

3: Both methods above can return the <strong>S</strong>um of
<strong>S</strong>quared <strong>R</strong>esiduals (<strong>SSR</strong>).
This is <strong>not</strong> the R^2 value. However, it is a part of the
calculation of R^2:

<br><br>
<strong>R^2 = 1 - (SSR / SST)</strong>
<br><br>

Where <strong>SST</strong> is the <strong>T</strong>otal <strong>S</strong>um of
<strong>S</strong>quares, you can obtain the SST by:

    SST = sum((y - np.mean(y))**2)

</details>
<details>
<summary>Solution</summary>

```python
a = np.arange(100)
b = 2 * a + 1 + rng.normal(scale=20, size=100)
ax.scatter(a, b, color=COLOR_BLUE, label='Random data')

# linalg.lstsq solution ==================================================
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

# Polynomial.fit solution ================================================
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
```

</details>

As a reminder this tutorial is not exhaustive, there are many
things you can do that we haven't even touched here (have a look at the
[examples](https://matplotlib.org/stable/gallery/index.html) on the official
documentation page for some fun ideas!) However if you've completed this
tutorial you should have the foundational skills to visualize data in just about
any way you can think of.
