import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из файла
data = np.loadtxt('output.V.T0_2700.txt', skiprows=1)  # пропуск заголовочной строки

# Извлечение данных
step = data[:, 0]
temperature = data[:, 1]

# Создание графика
plt.plot(step, temperature, label='Temperature vs Step')
plt.xlabel('Step')
plt.ylabel('Temperature')
plt.title('Temperature vs Step')
plt.legend()
plt.grid(True)
plt.show()
