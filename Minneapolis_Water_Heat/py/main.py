import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


start_year = 1960
end_year = 2021

# call file
path = '/Users/nathanoliver/Desktop/Python/Minneapolis_Water_Heat/csv/Assessors_Parcel_Data_2021.csv'

df = call_file(path)

print(df.columns)

print(df['PRIMARY_PROP_TYPE'].unique())
print(df.head(5))
print(df['LANDUSE'].unique())
# df['YEARBUILT']


# df[(df['PRIMARY_PROP_TYPE'] == 'SINGLE-FAMILY DETACHED DW')
#     or (df['PRIMARY_PROP_TYPE'] == 'SINGLE-FAMILY ATTACHED DW')]
df = df[df['BUILDINGUSE'] == 'SINGLE FAM. DWLG.']

# print(df.shape)

print(df['PRIMARYHEATING'].value_counts())


year = np.arange(start_year, end_year, 1)
count = np.zeros(len(year))

fa_count = np.zeros(len(year))
hw_count = np.zeros(len(year))
grav_count = np.zeros(len(year))
uh_count = np.zeros(len(year))
steam_count = np.zeros(len(year))
elec_count = np.zeros(len(year))
geo_count = np.zeros(len(year))
r_count = np.zeros(len(year))

df = df.reset_index()

# print(df)

for i in range(len(df)):
    n = df.loc[i, 'YEARBUILT']
    heat_fuel = df.loc[i, 'PRIMARYHEATING']

    index = np.where(year == n)
    count[index] = count[index] + 1

    if heat_fuel == 'FORCED AIR':
        fa_count[index] = fa_count[index] + 1
    if heat_fuel == 'HOT WATER':
        hw_count[index] = hw_count[index] + 1
    if heat_fuel == 'GRAVITY':
        grav_count[index] = hw_count[index] + 1
    if heat_fuel == 'UNIT HEATERS':
        uh_count[index] = hw_count[index] + 1
    if heat_fuel == 'STEAM':
        steam_count[index] = hw_count[index] + 1
    if heat_fuel == 'ELECTRIC':
        elec_count[index] = elec_count[index] + 1
    if heat_fuel == 'GEOTHERMAL':
        geo_count[index] = elec_count[index] + 1
    if heat_fuel == 'RADIANT FLOOR':
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
    'Minneapolis, MN\nSingle-Family Homes\nSpace Heat System Market Share', size=18)

ax2.set_facecolor(gray)
# ax1.plot(year, elec_count / count, label='Electric',
#          color=colors[0], linewidth=linewidth)
ax1.plot(year, fa_count / count, label='Forced Air',
         color=colors[3], linewidth=linewidth)
ax1.plot(year, hw_count / count, label='Hot Water Baseboard',
         color=colors[6], linewidth=linewidth)
# ax1.plot(year, grav_count / count, label='Gravity',
#          color=colors[1], linewidth=linewidth)
# ax1.plot(year, uh_count / count, label='Gravity',
#          color='black', linewidth=linewidth)
# ax1.plot(year, steam_count / count, label='Gravity',
#          color='brown', linewidth=linewidth)
ax1.plot(year, elec_count / count, label='Gravity',
         color=colors[0], linewidth=linewidth)
# ax1.plot(year, geo_count / count, label='Gravity',
#          color='red', linewidth=linewidth)
ax1.plot(year, r_count / count, label='Gravity',
         color=colors[1], linewidth=linewidth)

# plt.text(0.15, 0.21, 'Electric', weight='bold', size=m_size,
#          color=colors[0], transform=plt.gcf().transFigure)
plt.text(0.5, 0.77, 'Forced Air', weight='bold', size=m_size,
         color=colors[3], transform=plt.gcf().transFigure, ha="center", va="center")
plt.text(0.537, 0.31, 'Hot\nWater', weight='bold', size=m_size,
         color=colors[6], transform=plt.gcf().transFigure, ha="center", va="center")
plt.text(0.733, 0.32, 'Radiant', weight='bold', size=m_size,
         color=colors[1], transform=plt.gcf().transFigure)
plt.text(0.418, 0.22, 'Electric', weight='bold', size=m_size,
         color=colors[0], transform=plt.gcf().transFigure)
plt.text(0.32, 0.39, 'New Homes', weight='bold', size=m_size,
         color='#002746', transform=plt.gcf().transFigure)



upper_limit = 250

# plt.yticks(fontsize=l_size)
ax2.set_yticks(np.arange(0, upper_limit+50, 50))
ax2.set_yticklabels(np.arange(0, upper_limit+50, 50), size=l_size)
# ax2.set_yticklabels(['0', '600', '1200', '1800', '2400', '3000', '3600'])
ax2.set_xticks(np.arange(start_year, end_year, 5))
ax2.set_xticklabels(np.arange(start_year, end_year, 5), size=l_size)
ax1.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'], size=l_size)
ax1.grid(b=None, which='major', axis='y')
ax2.set_ylim(0, upper_limit)
ax1.set_ylim(0, 1)
ax2.set_xlim(start_year - 0.7, 2020 + 0.7)

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
# ax.set_xlim(start_year, 2019)

# plt.show()


# df_ng = df[df['Heat Fuel'] == 'Natural Gas']
# df_el = df[df['Heat Fuel'] == 'Electric']

# s = 0.01

# plt.scatter(df_ng['Longitude'], df_ng['Latitude'], color='blue', s=s)
# plt.scatter(df_el['Longitude'], df_el['Latitude'], color='red', s=.1)
# plt.show()
