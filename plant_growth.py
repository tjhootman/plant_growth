import matplotlib.pyplot as plt

# days and corresponding plant growth data
days = [1, 2, 3, 4, 5, 6, 7]
growth_type_a = [0.5, 1.2, 2.1, 3.0, 3.8, 4.5, 5.1]
growth_type_b = [0.3, 0.8, 1.5, 2.2, 2.9, 3.5, 4.0]
growth_type_c = [0.2, 0.5, 1.1, 1.8, 2.5, 3.1, 3.7]

# create a figure and axes
fig, ax = plt.subplots(figsize=(8,6))

# plot each line on the same axes
ax.plot(days, growth_type_a, label='Type A', marker='o', markersize=4)
ax.plot(days, growth_type_b, label='Type B', marker='o', markersize=4)
ax.plot(days, growth_type_c, label='Type C', marker='o', markersize=4)

# add titles and axis labels
ax.set_title('Growth of Bean Seed Types Over One Week')
ax.set_xlabel('Day')
ax.set_ylabel('Height (cm)')

# add a grid
ax.grid(True)

# add a legend
ax.legend()

# show the plot
# plt.show()

# save the figure
plt.savefig('plant_growth.png', bbox_inches='tight')
