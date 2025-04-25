import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]

growth_type_a = [0.5, 1.2, 2.1, 3.0, 3.8, 4.5, 5.1]

growth_type_b = [0.3, 0.8, 1.5, 2.2, 2.9, 3.5, 4.0]

growth_type_c = [0.2, 0.5, 1.1, 1.8, 2.5, 3.1, 3.7]

fig, ax = plt.subplots()

ax.plot(days, growth_type_a, linewidth=3)
ax.plot(days, growth_type_b, linewidth=3)
ax.plot(days, growth_type_c, linewidth=3)

plt.show()
