#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import sqrt


"""Napisz program, który pobiera od użytkownika dwie liczby rzeczywiste a i b, a następnie
wyświetla następujące informacje:
    - sumę i iloczyn liczb a i b,
    - wynik dzielenia a/b lub komunikat, że b jest równe 0 i nie można wykonać dzielenia,
    - wszystkie rzeczywiste rozwiązania układu równań a * x^2 + b * x + 1 lub informacje o braku
      rozwiązań,
    - pole i obwód trójkąta równoramiennego o podstawie a i wysokości b, lub zgłasza błąd jeśli
      a = 0 lub b = 0.
    """


if __name__ == '__main__':
    a, b = map(float, input('Podaj dwie liczby rzeczywiste oddzielone spacją: ').split())

    # Suma i iloczyn
    print(a, '+', b, '=', a + b)
    print(a, '*', b, '=', a * b)

    # Dzielenie
    if b == 0:
        print('Nie można wykonać dzielenia, ponieważ dzielnik jest równy 0.')
    else:
        print(a, '/', b, '=', a / b)

    # Rzeczywiste rozwiązania układu równań
    delta = b ** 2 - 4 * a
    if delta < 0:
        print('Układ równań nie ma rzeczywistych rozwązań.')
    elif delta == 0:
        print('Rzeczywistym rozwiązaniem układu równań jest liczba:', -b / (2*a))
    else:
        print('Rzeczywistymi rozwiązaniami układu równań są liczby:', (-b - sqrt(delta)) / (2 * a),
              ', oraz', (-b + sqrt(delta)) / (2 * a))

    # Pole i obwód trójkąta równoramiennego
    if a == 0 or b == 0:
        print('Trójkąt nie może posiadać boku o długości równej 0.')
    else:
        print('Pole trójkąta wynosi:', a * b / 2)
        print('Obwód trójkąta wynosi:', a + 2 * (sqrt((a / 2) ** 2 + b ** 2)))
