import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(sharex=True, figsize=(8, 8))


red = '#cc0000'
blue = 'blue'
gray = '#e0e0e0'

heating = [9971.1, 7234.7]
cooling = [0, 665.2]

width = 0.4
n = width / 2
x1 = [0 - n, 1 - n]
x2 = [0 + n, 1 + n]

title = 'Heating and Cooling Days\nAnchorage and Minneapolis'

ax.set_facecolor(gray)
ax.bar(x1, heating, width=width, color=red)
ax.bar(x2, cooling, width=width, color=blue)
ax.set_title(title, size=20)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Anchorage', 'Minneapolis'], size=15)
ax.set_yticks(np.arange(0, 12000, 2000))
ax.set_yticklabels(np.arange(0, 12000, 2000), size=15)
ax.legend(['Heating Days', 'Cooling Days'], fontsize=15)


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
