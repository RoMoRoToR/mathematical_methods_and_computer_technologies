import numpy as np
import matplotlib.pyplot as plt

# Параметры симуляции
N = 10  # Размер решетки
temperature_range = np.linspace(1, 4, 30)  # Диапазон температур
mc_steps = 10000  # Количество шагов Монте-Карло на каждой температуре

def initialize_lattice(N):
    lattice = np.random.choice([1, -1], size=(N, N))
    return lattice

def get_neighbors(i, j, N):
    neighbors = [
        ((i-1)%N, (j-1)%N), ((i-1)%N, j%N),
        (i%N, (j-1)%N), (i%N, (j+1)%N),
        ((i+1)%N, j%N), ((i+1)%N, (j+1)%N)
    ]
    return neighbors

def delta_energy(lattice, i, j):
    N = len(lattice)
    neighbors = get_neighbors(i, j, N)
    delta_E = 2 * lattice[i, j] * sum(lattice[x, y] for x, y in neighbors)
    return delta_E

def monte_carlo_step(lattice, beta):
    N = len(lattice)
    i, j = np.random.randint(0, N, size=2)
    delta_E = delta_energy(lattice, i, j)
    if delta_E < 0 or np.random.rand() < np.exp(-beta * delta_E):
        lattice[i, j] *= -1


def simulate(N, temperature_range, mc_steps):
    lattice = initialize_lattice(N)
    specific_heat_data = []
    susceptibility_data = []

    for T in temperature_range:
        beta = 1 / (T * 1)  # предполагается, что J=1
        E_avg, E2_avg, M_avg, M2_avg = 0, 0, 0, 0
        for step in range(mc_steps):
            monte_carlo_step(lattice, beta)
            E = -np.sum(lattice * (np.roll(lattice, 1, axis=0) + np.roll(lattice, 1, axis=1)))
            M = np.sum(lattice)
            E_avg += E / mc_steps
            E2_avg += E**2 / mc_steps
            M_avg += M / mc_steps
            M2_avg += M**2 / mc_steps
        C = (E2_avg - E_avg**2) * beta**2 / N**2
        chi = (M2_avg - M_avg**2) * beta / N**2
        specific_heat_data.append(C)
        susceptibility_data.append(chi)
        # Критическая температура T_c была определена как 3.5
    T_c = 3.5
    inverse_temp_diff = [1 / (T - T_c) for T in temperature_range if T > T_c]
    susceptibility_above_Tc = [chi for T, chi in zip(temperature_range, susceptibility_data) if T > T_c]

    # Построение графика
    plt.figure()
    plt.plot(inverse_temp_diff, susceptibility_above_Tc, 'o', label='Data')
    plt.xlabel('1/(T - Tc)')
    plt.ylabel('Susceptibility χ')
    plt.legend()
    plt.show()
    # Построение графика
    plt.figure(figsize=(20, 10))
    plt.subplot(2, 1, 1)
    plt.plot(temperature_range, specific_heat_data, label='Specific Heat')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(temperature_range, susceptibility_data, label='Susceptibility')
    plt.legend()
    plt.show()

simulate(N, temperature_range, mc_steps)
