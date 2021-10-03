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


fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, figsize=(20, 8))

colors = ['#ea4335', '#a460dc', '#edc948',
          '#34a853', '#76b7b2', '#4e79a7', '#4285f4']

colors1 = ['#34a853', '#4285f4', '#a460dc', '#e15759', 'black']
colors2 = ['#34a853', '#4285f4', '#edc948', 'black']


ax1.pie(df1.iloc[0, :], labels=df1.columns, colors=colors1)
ax2.pie(df2.iloc[0, :], labels=df2.columns, colors=colors2)

ax1.set_title('Anchorage, AK')
ax2.set_title('Minneapolis, MN')


plt.show()
