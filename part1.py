import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из файла
data = np.loadtxt('output.V.T0_2800.txt', skiprows=1)  # Предполагается, что файл находится в той же директории

# Разделение данных на отдельные массивы
steps, temperatures, densities, enthalpies = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

# Создание графика
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Step')
ax1.set_ylabel('Temperature (K)', color=color)
ax1.plot(steps, temperatures, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Density (g/cm^3)', color=color)
ax2.plot(steps, densities, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Temperature and Density vs Step')
plt.show()
