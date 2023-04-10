import matplotlib.pyplot as plt

united_states = [2.14, 2.44, 1.81, 1.23, 4.70]
canada = [1.60, 2.27, 1.95, 0.72, 3.40]

print(plt.style.available)

for style in plt.style.available:
    plt.style.use(style)
    plt.plot(united_states)
    plt.plot(canada)
    plt.title(style.capitalize())
    plt.show()
