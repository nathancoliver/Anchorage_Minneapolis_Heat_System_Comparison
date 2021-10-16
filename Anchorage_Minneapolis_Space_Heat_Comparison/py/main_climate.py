import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import interp2d


pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file
path1 = '/Users/nathanoliver/Desktop/Python/Anchorage_Minneapolis_Space_Heat_Comparison/csv/anchorage_climate_data.csv'
path2 = '/Users/nathanoliver/Desktop/Python/Anchorage_Minneapolis_Space_Heat_Comparison/csv/minneapolis_climate_data.csv'


df1 = call_file(path1)
df2 = call_file(path2)

# df1["cbsa_code"] = pd.to_numeric(df1["cbsa_code"])

print(df1.columns)
print(df1.dtypes)

print(df2.columns)
print(df2.dtypes)

def curved_line(x, y, color, linestyle, label):

    cubic_interpolation_model = interp1d(
        x, y, kind='quadratic')
    x_new = np.linspace(x.min(), x.max(), 500)
    y_new = cubic_interpolation_model(x_new)
    plot_new(x_new, y_new, color, linestyle, label)
    return x_new, y_new


def plot_new(x_new, y_new, color, linestyle, label):
    ax.set_xlim(1, 12)
    ax.set_ylim(0, 90)
    ax.set_xlabel('Month', size=15)
    ax.set_ylabel('Temperature ($^\circ$F)', size=15)
    ax.set_title(
        'Anchorage, AK and Minneapolis, MN\nMonthly Temperature Comparison', size=18)
    ax.set_xticks(np.arange(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], size=13.5)
    ax.set_yticks(np.arange(0, 100, 10))
    ax.set_yticklabels(np.arange(0, 100, 10), size=13.5)
    ax.plot(x_new, y_new, color=color, linestyle=linestyle, label=label)


fig, ax = plt.subplots(sharex=True, figsize=(20, 8))


curved_line(np.arange(1, 14),
            df2.loc[:, 'average_high'], color='red', linestyle='--', label='MSP Average High')
curved_line(np.arange(1, 14),
            df2.loc[:, 'daily_mean'], color='black', linestyle='--', label='MSP Daily Mean')
print(df1)
curved_line(np.arange(1, 14),
            df2.loc[:, 'average_low'], color='blue', linestyle='--', label='MSP Average Low')
curved_line(np.arange(1, 14),
            df1.loc[:, 'average_high'], color='red', linestyle='-', label='ANC Average High')
curved_line(np.arange(1, 14),
            df1.loc[:, 'daily_mean'], color='black', linestyle='-', label='ANC Daily Mean')
print(df1)
curved_line(np.arange(1, 14),
            df1.loc[:, 'average_low'], color='blue', linestyle='-', label='ANC Average High')


ax.legend()


# ax.plot(x_new, y_new)


# colors = ['#ea4335', '#a460dc', '#edc948',
#           '#34a853', '#76b7b2', '#4e79a7', '#4285f4']

# colors1 = ['#34a853', '#4285f4', '#a460dc', '#e15759', 'grey']
# colors2 = ['#34a853', '#4285f4', '#edc948', 'grey']

# label_size = 12

# ax1.pie(df1.iloc[0, :] / sum(df1.iloc[0, :]), labels=labels1,
#         colors=colors1, pctdistance=1.3, labeldistance=0.5, textprops=dict(ha='center', va='center', weight='bold', size=label_size))

# ax2.pie(df2.iloc[0, :] / sum(df2.iloc[0, :]), labels=labels2, colors=colors2,
#         pctdistance=1.3, labeldistance=0.5, textprops=dict(ha='center', va='center', weight='bold', size=label_size))


# sub_title_size = 15
# main_title_size = 20
# ax1.set_title('Anchorage, AK', size=sub_title_size)
# ax2.set_title('Minneapolis, MN', size=sub_title_size)
# fig.suptitle('Single-Family Home\nSpace Heat System Comparison',
#              size=main_title_size)

# ax1.text(1.35, 0.2, 'Other\n0.3%', color='black',
#          weight='bold', size=label_size, ha="center", va="center")

# ax1.text(1.4, -0.1, 'Electric\n1.4%', color='black',
#          weight='bold', size=label_size, ha="center", va="center")

# ax1.text(1.35, -0.4, 'Radiant\n 3.0%', color='black',
#          weight='bold', size=label_size, ha="center", va="center")

# ax2.text(1.4, 0, 'Other\n0.7%', color='black',
#          weight='bold', size=label_size, ha="center", va="center")

# ax2.text(1.4, -0.25, 'Gravity\n3.6%', color='black',
#          weight='bold', size=label_size, ha="center", va="center")

# ax1.plot((1.2, 1), (0.2, 0), color='black', linewidth=1)
# ax1.plot((1.2, 1), (-0.1, -0.05), color='black', linewidth=1)
# ax1.plot((1.15, 0.98), (-0.35, -0.2), color='black', linewidth=1)

# ax2.plot((1.23, 1), (0.03, -0.02), color='black', linewidth=1)
# ax2.plot((1.18, 0.99), (-0.2, -0.15), color='black', linewidth=1)

# # 'Gravity\n 3.6%', 'Other\n0.7%'
# # 'Radiant\n 3.0%', 'Electric\n1.4%', 'Other\n0.3%'

plt.show()
