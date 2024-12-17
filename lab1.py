# autor: Dominik Kaczmarek 281007

"""
Program liczący pierwiastki trójmianu kwadratowego.
    a) Dla danych z klawiatury
    b) Pytający użytkownika o kontynuację obliczeń
    c) Odporny na błędne dane
"""

import math


# funkcja obliczająca deltę
def delta(a: int, b: int, c: int):
    return b ** 2 - (4 * a * c)


# funkcja obliczająca pierwiastki
def pierwiastki(a: int, b: int, c: int):
    if a == 0:
        print("Współczynnik A nie może byc równy 0.")
        return
    d = delta(a, b, c)
    if d == 0:
        x0 = -b / (2 * a)
        print(f"Równanie ma pierwiastek podwójny x0 = {x0}")
    elif d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(f"Równanie ma dwa rozwiązania: x1 = {x1}, x2 = {x2}")
    else:
        print(f"Równanie nie ma rozwiązań")


# funkcja pytająca, czy kontynuować liczenie
def czy_kontynuowac_liczenie():
    o = input("Czy chcesz kontynuować liczenie? (T/N): ")
    if o == "T" or o == "t":
        return True
    else:
        return False


print("Program oblicza pierwiastki równania kwadratowego w formacie Ax + By + C = 0")
poprawne = False
kontynuuj = True
while kontynuuj:
    while not poprawne:
        try:
            a = int(input("Wprowadź współczynnik A: "))
            b = int(input("Wprowadź współczynnik B: "))
            c = int(input("Wprowadź współczynnik C: "))
            pierwiastki(a, b, c)
            poprawne = True
            kontynuuj = czy_kontynuowac_liczenie()
        except ValueError:
            print("Podano niepoprawne dane")
