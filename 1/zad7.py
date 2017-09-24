#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from sys import argv
from math import sqrt


"""Napisz program, którego argumentem jest nazwa pliku zawierającego po trzy 
liczby w wierszu ( pierwsza niezerowa). Program dla każdego wiersza: - 
potraktuje te liczby jako współczynniki trójmianu kwadratowego ax^2 + bx + 
c, obliczy i wypisze pierwiastki rzeczywiste (jeśli są dwa), pierwiastek (
jeśli jeden), lub informację o ich braku, na koniec podsumuje, ile trójmianów 
miało 0, 1, 2 pierwiastków.
"""


if __name__ == '__main__':
    with open(argv[1], 'r') as plik:
        zero = jeden = dwa = 0
        for linia in plik:
            x = list(map(int, linia.split()))
            delta = x[1] ** 2 - 4 * x[0] * x[2]

            if delta < 0:
                print('Brak pierwiastków.')
                zero += 1
            elif delta == 0:
                print(-x[1] / (2 * x[0]))
                jeden += 1
            else:
                print((-x[1] - sqrt(delta)) / (2 * x[0]),
                      (-x[1] - sqrt(delta)) / (2 * x[0]))
                dwa += 1

        print('\nPodsumowanie:')
        print('\t0 pierwiastków:\t{}'.format(zero))
        print('\t1 pierwiasek:\t{}'.format(jeden))
        print('\t2 pierwiastki:\t{}'.format(dwa))
