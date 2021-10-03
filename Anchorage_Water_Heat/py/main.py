import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file
path = '/Users/nathanoliver/Desktop/Python/Anchorage_Water_Heat/csv/MoA_anchorage_property_information.csv'
df = call_file(path)

print(df.columns)

df['Year Built']
df['Effective Year']

df[df['Property Type'] == 'Residential']
df[df['Land Use'] == 'Single Family']

print(df['Heat Type'].value_counts())
print(df['Heat Fuel'].value_counts())
print(df['Heat System'].value_counts())


# df.info()

year = np.arange(1960, 2020, 1)
count = np.zeros(len(year))
elec_count = np.zeros(len(year))

fa_count = np.zeros(len(year))
hw_count = np.zeros(len(year))
r_count = np.zeros(len(year))


for i in range(len(df)):
    n = df.loc[i, 'Effective Year']
    heat_fuel = df.loc[i, 'Heat System']

    index = np.where(year == n)
    count[index] = count[index] + 1

    if heat_fuel == 'Electric':
        elec_count[index] = elec_count[index] + 1
    if heat_fuel == 'Forced Air':
        fa_count[index] = fa_count[index] + 1
    if heat_fuel == 'Hot Water':
        hw_count[index] = hw_count[index] + 1
    if heat_fuel == 'Radiant':
        r_count[index] = r_count[index] + 1


# plot year built graph

fig, ax2 = plt.subplots(sharex=True, figsize=(14, 7))


linewidth = 3
m_size = 15
l_size = 12
# gray = '#a9a9a9'
# gray = '#ECECEC'
# gray = '#c0c0c0'
gray = '#d3d3d3'
gray = '#e0e0e0'

colors = ['#e15759', '#f28e2b', '#edc948',
          '#59a14f', '#76b7b2', '#4e79a7', '#b07aa1']

colors = ['#ea4335', '#a460dc', '#edc948',
          '#34a853', '#76b7b2', '#4e79a7', '#4285f4']

ax2.bar(year, count, color='#002746')

# ax1.bar(year, elec_count, color='red')

# plt.bar(year, np.ones(len(year)))

ax1 = ax2.twinx()

ax1.set_title(
    'Anchorage, AK\nSingle-Family Homes\nSpace Heat System Market Share', size=18)

ax2.set_facecolor(gray)
ax1.plot(year, elec_count / count, label='Electric',
         color=colors[0], linewidth=linewidth)
ax1.plot(year, fa_count / count, label='Forced Air',
         color=colors[3], linewidth=linewidth)
ax1.plot(year, hw_count / count, label='Hot Water Baseboard',
         color=colors[6], linewidth=linewidth)
ax1.plot(year, r_count / count, label='Radiant Floor Heating',
         color=colors[1], linewidth=linewidth)

plt.text(0.15, 0.21, 'Electric', weight='bold', size=m_size,
         color=colors[0], transform=plt.gcf().transFigure)
plt.text(0.54, 0.8, 'Forced Air', weight='bold', size=m_size,
         color=colors[3], transform=plt.gcf().transFigure)
plt.text(0.54, 0.34, 'Hot Water', weight='bold', size=m_size,
         color=colors[6], transform=plt.gcf().transFigure)
plt.text(0.78, 0.28, 'Radiant', weight='bold', size=m_size,
         color=colors[1], transform=plt.gcf().transFigure)
plt.text(0.293, 0.4, 'New Homes', weight='bold', size=m_size,
         color='#002746', transform=plt.gcf().transFigure)


# plt.yticks(fontsize=l_size)
ax2.set_yticks(np.arange(0, 9000, 1500))
ax2.set_yticklabels(np.arange(0, 9000, 1500), size=l_size)
ax2.set_xticks(np.arange(1960, 2020, 5))
ax2.set_xticklabels(np.arange(1960, 2020, 5), size=l_size)
ax1.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'], size=l_size)
ax1.grid(b=None, which='major', axis='y')
ax2.set_ylim(0, 7500)
ax1.set_ylim(0, 1)
ax2.set_xlim(1960 - 0.7, 2019 + 0.7)

plt.text(0.05, 0.48, '    Annual\nNew Homes', weight='bold',
         transform=plt.gcf().transFigure)
plt.text(0.91, 0.47, '    New Home\n  Heat System\n Annual Share', weight='bold',
         transform=plt.gcf().transFigure)

# ax2.set_ylabel('Annual\nNew Homes', rotation='horizontal')
# ax1.set_ylabel('New Home\nEnergy System\nAnnual Share',
#                rotation='horizontal', labelpad=10)

plt.show()

# fig, ax = plt.subplots()

# d = 0.1
# width = 0.2

# ax.bar(year - 3 * d, elec_count / count,
#        color='red', label='Electric', width=width)
# ax.bar(year - d, fa_count / count, color='green',
#        label='Forced Air', width=width)
# ax.bar(year + d, hw_count / count, color='blue',
#        label='Hot Water', width=width)
# ax.bar(year + 3 * d, r_count / count,
#        color='black', label='Radiant', width=width)
# ax.set_xlim(1960, 2019)

# plt.show()


# df_ng = df[df['Heat Fuel'] == 'Natural Gas']
# df_el = df[df['Heat Fuel'] == 'Electric']

# s = 0.01

# plt.scatter(df_ng['Longitude'], df_ng['Latitude'], color='blue', s=s)
# plt.scatter(df_el['Longitude'], df_el['Latitude'], color='red', s=.1)
# plt.show()
