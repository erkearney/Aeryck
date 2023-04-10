import matplotlib.pyplot as plt

united_states = [2.14, 2.44, 1.81, 1.23, 4.70]
canada = [1.60, 2.27, 1.95, 0.72, 3.40]
years = [2017, 2018, 2019, 2020, 2021]

fig, ax = plt.subplots()
# let's set some colorblind-friendly colors
US_COLOR = '#3182bd' # blue
CA_COLOR = '#de2d26' # red

ax.plot(years, united_states, color=US_COLOR, linewidth=2, label='United States')
ax.plot(years, canada, color=CA_COLOR, linewidth=2, label='Canada')

# get rid of some clutter
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# add some horizontal gridlines
ax.yaxis.grid(color='gray', linestyle='dashed')

ax.set_title('Inflation in the United States and Canada', weight='bold')
ax.set_xlabel('Year', weight='bold')
ax.set_ylabel('Percent', weight='bold')

# add a subtitle
ax.text(0.5, 0.98, 'Average annual headline consumer price inflation (source: World Bank)', transform=ax.transAxes, ha='center', fontsize=8)

# adjust interval on x-axis
ax.set_xticks(years)
ax.set_xticklabels(years)

ax.legend(loc='lower left')

plt.show()
