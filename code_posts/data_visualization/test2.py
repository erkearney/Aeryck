import matplotlib.pyplot as plt

united_states = [2.14, 2.44, 1.81, 1.23, 4.70]
years = [2017, 2018, 2019, 2020, 2021]

us_dict = {'Year': years, 'Percent': united_states}

fig, ax = plt.subplots()
ax.plot('Year', 'Percent', data=us_dict)

plt.show()
