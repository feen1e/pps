# autor: Dominik Kaczmarek 281007

"""
Stworzyć i wyświetlić sygnał sinusoidalny:
    • Czas trwania = 5s
    • Częstotliwość próbkowania = 100Hz
    • Częstotliwość sygnału = 7Hz
    • Amplituda = 3
"""

import numpy as np
import matplotlib.pyplot as plt

czas = 5
czetotliwosc_probkowania = 100
czestotliwosc_sygnalu = 7
amplituda = 3

x = np.arange(0, czas, (1/czetotliwosc_probkowania))
y = np.sin(2 * np.pi * czestotliwosc_sygnalu * x) * amplituda

plt.plot(x, y)
plt.show()