# autor: Dominik Kaczmarek 281007

"""
1. Na sygnale z poprzednich zajęć zastosować filtr butterwortha:
    a) Dolnoprzepustowy (pozostawić jedynie najmniejszą częstotliwość)
    b) Górnoprzepustowy (pozostawić jedynie największą częstotliwość)
    c) Pasmowo przepustowy (pozostawić jedynie środkową częstotliwość)
2. W jednym oknie przedstawić sygnał oryginalny i sygnały po zastosowaniu wszystkich filtrów
3. W jednym oknie przedstawić FFT wszystkich sygnałów
4. Przedstawić spectrogram sygnału oryginalnego
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

czas = 1
czetotliwosc_probkowania = 1000
czestotliwosc_sygnalu = 50
amplituda = 3

x = np.arange(0, czas, (1 / czetotliwosc_probkowania))
y = np.sin(2 * np.pi * czestotliwosc_sygnalu * x) * amplituda

# dodanie dwóch składowych
y_dodatkowe = y + np.sin(2 * np.pi * 150 * x) * amplituda + np.sin(2 * np.pi * 300 * x) * amplituda

# dodanie wykresu sygnału
plt.figure(1)
plt.subplot(4, 1, 1)
plt.plot(x, y_dodatkowe)

# stworzenie filtrów i dodanie wykresów przefiltrowanych sygnałów
order = 4
b, a = butter(order, 50, btype="lowpass", fs=czetotliwosc_probkowania)
y_low = filtfilt(b, a, y_dodatkowe)
plt.subplot(4, 1, 2)
plt.plot(x, y_low)

b, a = butter(order, [100, 200], btype="bandpass", fs=czetotliwosc_probkowania)
y_band = filtfilt(b, a, y_dodatkowe)
plt.subplot(4, 1, 3)
plt.plot(x, y_band)

b, a = butter(order, 250, btype="highpass", fs=czetotliwosc_probkowania)
y_high = filtfilt(b, a, y_dodatkowe)
plt.subplot(4, 1, 4)
plt.plot(x, y_high)

# stworzenie i dodanie wykresów fft każdego z poprzednich sygnałów
N = int(len(y_dodatkowe) / 2)
plt.figure(2)
plt.subplot(4, 1, 1)
plt.plot(x[:N], np.abs(np.fft.fft(y_dodatkowe)[:N]))

plt.subplot(4, 1, 2)
plt.plot(x[:N], np.abs(np.fft.fft(y_low)[:N]))

plt.subplot(4, 1, 3)
plt.plot(x[:N], np.abs(np.fft.fft(y_band)[:N]))

plt.subplot(4, 1, 4)
plt.plot(x[:N], np.abs(np.fft.fft(y_high)[:N]))

# dodanie spectrogramu oryginalnego sygnału
plt.figure(3)
plt.specgram(y_dodatkowe)
# pokazanie wykresów
plt.show()