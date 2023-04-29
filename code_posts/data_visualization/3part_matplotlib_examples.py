import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

united_states = [2.14, 2.44, 1.81, 1.23, 4.70]
canada = [1.60, 2.27, 1.95, 0.72, 3.40]
years = [2017, 2018, 2019, 2020, 2021]

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(united_states)
ax1.plot(canada)

US_COLOR = '#3182bd' # blue
CA_COLOR = '#de2d26' # red

ax2.plot(years, united_states, color=US_COLOR, linewidth=2, label='United States')
ax2.plot(years, canada, color=CA_COLOR, linewidth=2, label='Canada')

# get rid of some clutter
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# add some horizontal gridlines
ax2.yaxis.grid(color='gray', linestyle='dashed')

ax2.set_title('Inflation in the United States and Canada', weight='bold')
ax2.set_xlabel('Year', weight='bold')
ax2.set_ylabel('Percent', weight='bold')

# add a subtitle
ax2.text(0.5, 0.98, 'Average annual headline consumer price inflation (source: World Bank)', transform=ax2.transAxes, ha='center', fontsize=8)

# adjust interval on x-ax2is
ax2.set_xticks(years)
ax2.set_xticklabels(years)

ax2.legend(loc='lower left')

plt.show()

# ============================================================================
# animation section
# ============================================================================

CA_COLOR = '#6699CC'
CO_COLOR = '#33CC66'
DATA_LOC = '../not_my_data/Minimum Wage Data.csv'

# data source: https://www.kaggle.com/datasets/lislejoem/us-minimum-wage-by-state-from-1968-to-2017
df = pd.read_csv(DATA_LOC, encoding='Windows-1252')
years = pd.unique(df['Year'])
california = list(df.loc[df['State'] == 'California', 'State.Minimum.Wage'])
colorado = list(df.loc[df['State'] == 'Colorado', 'State.Minimum.Wage'])

fig, ax = plt.subplots()
ax.set_title('Minimum Wage (hourly) in California and Colorado', weight='bold')
ax.text(0.5, 0.98, 'Source: U.S. Department of Labor', transform=ax.transAxes, ha='center', fontsize=8)
ax.set_xlabel('Year', weight='bold')
ax.set_ylabel('State minimum wage ($)', weight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.set(xlim=[years[0], years[-1]], ylim=[0, 15])

ca_line = ax.plot(years, california, color=CA_COLOR, label='California')
co_line = ax.plot(years, colorado, color=CO_COLOR, label='Colorado')
ax.legend(loc='lower right')

ca_line = ca_line[0]
co_line = co_line[0]

INTERVAL = 30
SECONDS_BETWEEN_REPEAT = 2
FRAMES = len(years) + int((SECONDS_BETWEEN_REPEAT*1000)/INTERVAL)

def update(frame):
    if frame < len(years):
        ca_line.set_xdata(years[:frame])
        ca_line.set_ydata(california[:frame])

        co_line.set_xdata(years[:frame])
        co_line.set_ydata(colorado[:frame])

    return (ca_line, co_line)


ani = animation.FuncAnimation(fig=fig, func=update, frames=FRAMES, interval=INTERVAL, repeat=True)
#ani.save(filename='state_min_wage.gif', writer='pillow')

plt.show()


# unfortunately the data did not contain federal data, so I'm hard-coding
federal_min_wages = [1.6, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.1, 2.3, 2.65, 2.65,
2.9, 3.1, 3.35, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 4.25, 4.75, 4.75,
4.75, 4.75, 4.75, 5.15, 5.85, 5.85, 5.85, 5.85, 5.85, 5.85, 5.85, 5.85, 5.85,
5.85, 6.55, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25,
7.25]

DATA_LOC = '../not_my_data/Minimum Wage Data.csv'
df = pd.read_csv(DATA_LOC, encoding='Windows-1252')
state_names = pd.unique(df['State'])
years = pd.unique(df['Year'])
num_years = len(years)

states = {}
for state_name in state_names:
    min_wage_data = list(df.loc[df['State'] == state_name, 'State.Minimum.Wage'])
    if np.allclose(min_wage_data, 0):
        continue

    states[state_name] = list(df.loc[df['State'] == state_name, 'State.Minimum.Wage'])

states = dict(sorted(states.items(), key=lambda item: item[0], reverse=True))

average_wages = []
for year in years:
    wages = np.average(np.array(df.loc[df['Year'] == year, 'State.Minimum.Wage']))
    average_wages.append(wages)


COLOR_RED = '#DE2D26'
COLOR_BLUE = '#6699CC'
COLOR_GREEN = '#33CC66'

fig, ax = plt.subplots()
ax.set_xlim([0, 15])
ax.set_xlabel('Hourly Minimum Wage ($)', weight='bold')
ax.set_ylabel('State, Territory, or District', fontsize=12, weight='bold')
ax.set_title('Minimum Wage in The United States', weight='bold')

def currency(x, pos):
    return f'${x:.2f}'

ax.xaxis.set_major_formatter(currency)

fig.text(0.80, 0.01, '*Alabama, Louisiana, Mississippi, South Carolina,\nand Tennessee have no minimum wage laws', ha='center')

txt = ax.text(0.92, 0.96, f'Year: {years[0]}', transform=ax.transAxes, weight='bold', fontsize=16)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.xaxis.grid(True, linestyle='--', color='gray', alpha=0.4)
starting_min_wages = [x[0] for x in states.values()]
state_names = list(states.keys())
bars = ax.barh(state_names, starting_min_wages)

starting_federal_min_wage = federal_min_wages[0]
federal_line = ax.axvline(starting_federal_min_wage, ls='--', linewidth=2, color=COLOR_GREEN, label='Federal')
blue_patch = matplotlib.patches.Patch(color=COLOR_BLUE, label='Above Average')
red_patch = matplotlib.patches.Patch(color=COLOR_RED, label='Below Average')
ax.legend(handles=[blue_patch, red_patch, federal_line], loc='lower right')

INTERVAL = 250
SECONDS_BETWEEN_REPEAT = 1
FRAMES = num_years + int((SECONDS_BETWEEN_REPEAT*1000)/INTERVAL)

def update(frame):
    if frame < num_years:
        txt.set_text(f'Year: {years[frame]}')
        federal_line.set_xdata([federal_min_wages[frame]])

        average_wage = average_wages[frame]
        for i, rectangle in enumerate(bars.patches):
            state = state_names[i]
            min_wage = states[state][frame]
            rectangle.set_width(min_wage)
            if min_wage < average_wage:
                rectangle.set_color(COLOR_RED)
            else:
                rectangle.set_color(COLOR_BLUE)

    return bars.datavalues

ani = animation.FuncAnimation(fig=fig, func=update, frames=FRAMES, interval=INTERVAL, repeat=True)

plt.show()

#ani.save(filename='all_states_min_wage.html', writer='html')
