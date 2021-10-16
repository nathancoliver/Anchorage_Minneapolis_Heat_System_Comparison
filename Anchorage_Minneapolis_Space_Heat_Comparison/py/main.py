import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# call file function

# start_year = 1960
# end_year = 2021


# def call_file(path):
#     data = pd.read_csv(path)
#     return pd.DataFrame(data)


# # call file
# path = '/Users/nathanoliver/Desktop/Python/Anchorage_Water_Heat/csv/MoA_anchorage_property_information.csv'

# Anchorage
# Forced Air             39044
# Hot Water              35465
# Radiant                 2360
# Electric                1131
# None                     106
# Hybrid Space Heater       91
# Solar                      3

# Minneapolis
# FORCED AIR       50176
# HOT WATER        17999
# GRAVITY           2555
# UNIT HEATERS       193
# STEAM              123
# ELECTRIC           115
# GEOTHERMAL          31
# RADIANT FLOOR       22

data = {'city': ['Anchorage', 'Minneapolis'], 'forced air': [
    39044, 50176], 'hot water': [35465, 17999], 'gravity': [0, 2555], 'radiant': [2360, 22], 'electric': [1131, 115], 'none': [106, 0], 'space heater': [91, 193], 'solar': [3, 0],
    'steam': [0, 123], 'geothermal': [0, 31]}


other1 = 106 + 91 + 3
other2 = 22 + 115 + 193 + 123 + 31

data1 = {'forced air': [39044], 'hot water': [35465],
         'radiant': [2360], 'electric': [1131], 'other': [other1]}
data2 = {'forced air': [50176], 'hot water': [
    17999], 'gravity': [2555], 'other': [other2]}


# df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

label1_numbers = df1.iloc[0, :]
label1 = ['', '', '', '', '']
print(label1[0])

labels1 = ['Forced Air\n49.9%', 'Hot Water\n45.4%', '', '', '']
labels2 = ['Forced Air\n70.5%', 'Hot Water\n25.3%', '', '']


# label1_columns = df1.columns

# for i in range(5):
#     label1[i] = label1_columns[i] + ' ' + label1_numbers[i]
#     print(i)
#     # label1[i] = i

# print(label1)


fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, figsize=(20, 8))

colors = ['#ea4335', '#a460dc', '#edc948',
          '#34a853', '#76b7b2', '#4e79a7', '#4285f4']

colors1 = ['#34a853', '#4285f4', '#a460dc', '#e15759', 'grey']
colors2 = ['#34a853', '#4285f4', '#edc948', 'grey']

label_size = 12

ax1.pie(df1.iloc[0, :] / sum(df1.iloc[0, :]), labels=labels1,
        colors=colors1, pctdistance=1.3, labeldistance=0.5, textprops=dict(ha='center', va='center', weight='bold', size=label_size))

ax2.pie(df2.iloc[0, :] / sum(df2.iloc[0, :]), labels=labels2, colors=colors2,
        pctdistance=1.3, labeldistance=0.5, textprops=dict(ha='center', va='center', weight='bold', size=label_size))


sub_title_size = 15
main_title_size = 20
ax1.set_title('Anchorage, AK', size=sub_title_size)
ax2.set_title('Minneapolis, MN', size=sub_title_size)
fig.suptitle('Single-Family Home\nSpace Heat System Comparison',
             size=main_title_size)

ax1.text(1.35, 0.2, 'Other\n0.3%', color='black',
         weight='bold', size=label_size, ha="center", va="center")

ax1.text(1.4, -0.1, 'Electric\n1.4%', color='black',
         weight='bold', size=label_size, ha="center", va="center")

ax1.text(1.35, -0.4, 'Radiant\n 3.0%', color='black',
         weight='bold', size=label_size, ha="center", va="center")

ax2.text(1.4, 0, 'Other\n0.7%', color='black',
         weight='bold', size=label_size, ha="center", va="center")

ax2.text(1.4, -0.25, 'Gravity\n3.6%', color='black',
         weight='bold', size=label_size, ha="center", va="center")

ax1.plot((1.2, 1), (0.2, 0), color='black', linewidth=1)
ax1.plot((1.2, 1), (-0.1, -0.05), color='black', linewidth=1)
ax1.plot((1.15, 0.98), (-0.35, -0.2), color='black', linewidth=1)

ax2.plot((1.23, 1), (0.03, -0.02), color='black', linewidth=1)
ax2.plot((1.18, 0.99), (-0.2, -0.15), color='black', linewidth=1)

# 'Gravity\n 3.6%', 'Other\n0.7%'
# 'Radiant\n 3.0%', 'Electric\n1.4%', 'Other\n0.3%'

plt.show()
