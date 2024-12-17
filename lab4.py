# autor: Dominik Kaczmarek 281007

"""
Program implementujący DFT = Σ Xn e^((-2πjkn)/ N) √(Re^2 + Im^2)
    Gdzie:
    • Xn - próbka nr n
    • e - np.exp
    • j - jednostka urojona
    • k = n.reshape((N, 1))
    • N - liczba próbek
a. Do sygnału z poprzednich zajęć dodać 2 składowe o różnych częstotliwościach i amplitudach
b. Wyświetlić na jednym plocie oryginalny sygnał sinusoidalny i DFT
c. Na wykresie DFT uwzględnić tylko pierwszą połowę sygnału
d. Dodać funkcję FFT z biblioteki numpy i porównać czas wykonywania obu algorytmów
"""

import time
import numpy as np
import matplotlib.pyplot as plt

czas = 5
czetotliwosc_probkowania = 100
czestotliwosc_sygnalu = 7
amplituda = 3

x = np.arange(0, czas, (1 / czetotliwosc_probkowania))
y = np.sin(2 * np.pi * czestotliwosc_sygnalu * x) * amplituda

# dodanie dwóch składowych
y_dodatkowe = y + np.sin(2 * np.pi * 5 * x) * 2 + np.sin(2 * np.pi * 10 * x)


# funkcja obliczająca dft
def dft(sygnal):
    N = len(sygnal)
    n = np.arange(N)
    k = n.reshape(N, 1)
    e = (-2j * np.pi * k * n) / N
    wynik = np.dot(sygnal, np.exp(e))
    return wynik


# zmierzenie czasu dft i dodanie do wykresu
dft_start = time.perf_counter()
dft_wynik = dft(y_dodatkowe)
dft_koniec = time.perf_counter()
print("DFT: " + str(dft_koniec - dft_start))

N = int(len(y_dodatkowe) / 2)
plt.plot(x[:N], np.abs(dft_wynik[:N]))

# zmierzenie czasu fft
fft_start = time.perf_counter()
fft_wynik = np.fft.fft(y_dodatkowe)
fft_koniec = time.perf_counter()
print("FFT: " + str(fft_koniec - fft_start))

# dodanie oryginalnego sygnału do wykresu
plt.plot(x, y_dodatkowe)
plt.show()
