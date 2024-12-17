# autor: Dominik Kaczmarek 281007

"""
Program realizujący funkcję zegara
    a. Dla godziny początkowej zadanej z klawiatury w formacie HH:MM:SS
    b. Program odporny na błędne wprowadzenie danych
    c. Dający wybór trybu: tradycyjny zegar i minutnik
    d. Alarm dźwiękowy w trybie minutnika
"""

import time
import winsound


def zegar(h, m, s):
    while True:
        print(f"{h}:{m}:{s}")
        time.sleep(1)
        s += 1
        if s == 60:
            m += 1
            s = 0
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0


def minutnik(h, m, s):
    while h != 0 or m != 0 or s != 0:
        print(f"{h}:{m}:{s}")
        time.sleep(1)
        s -= 1
        if s == -1 and m > 0:
            s = 59
            m -= 1
            if m == -1 and h > 0:
                h -= 1
                m = 59

    print("00:00:00")
    winsound.Beep(500, 1000)


godzina = 0
minuta = 0
sekunda = 0
poprawne = False
tryb = 0

while not poprawne:
    try:
        tryb = int(input("Wybierz tryb działania: zegar (0) lub minutnik(1): "))
        if tryb > 1 or tryb < 0:
            print("Tryb dzialania musi byc 0 lub 1")
            continue
        godzina = int(input("Podaj godziny: "))
        minuta = int(input("Podaj minuty: "))
        sekunda = int(input("Podaj sekundy: "))
        poprawne = True
    except ValueError:
        print("Podano niepoprawne dane")
        print(f"Czas początkowy: {godzina}:{minuta}:{sekunda}")
    if tryb == 0:
        zegar(godzina, minuta, sekunda)
    else:
        minutnik(godzina, minuta, sekunda)
