import matplotlib.pyplot as plt
import numpy as np

# Функция для загрузки данных
def load_data(filename):
    data = np.loadtxt(filename, skiprows=1)  # пропуск заголовочной строки
    enthalpy = data[:, 3]  # извлечение данных энтальпии
    temperature = data[:, 1]  # извлечение данных температуры
    return enthalpy, temperature

# Загрузка данных из файлов
enthalpy_2700, temperature_2700 = load_data('output.V.T0_2700.txt')
enthalpy_2800, temperature_2800 = load_data('output.V.T0_2800.txt')

# Создание графика
plt.plot(enthalpy_2700, temperature_2700, '-', label='T0=2700')
plt.plot(enthalpy_2800, temperature_2800, '-', label='T0=2800')
plt.xlabel('Enthalpy')
plt.ylabel('Temperature')
plt.title('Temperature vs Enthalpy')
plt.legend()
plt.grid(True)
plt.show()
