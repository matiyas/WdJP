#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Zaimplementuj na dwa sposoby (rekurencyjnie oraz iteracyjnie) funkcję silnia. Funkcje powinny
wypisywać (w czytelny w zrozumiały sposób) na ekran tablicę swoich zmiennych lokalnych oraz
globalnych.
    W jaki sposób zmieniają się zmienne lokalne i globalne w zależności od sposobu implementacji
    (rekurencja kontra iteracja)?"""


def silnia_iteracyjnie(n):
    silnia = 1
    for x in range(2, n + 1):
        silnia *= x
        # Zmienne lokalne
        print('\nZmienne lokalne funkcji silnia_iteracyjnie:')
        for zmienna, wartosc in zip(locals().keys(), locals().values()):
            if zmienna != '__doc__':
                print('\t{:>20} = {}'.format(zmienna, wartosc))

        # Zmienne globalne
        print('\nZmienne globalne funkcji silnia_iteracyjnie:')
        for zmienna, wartosc in zip(globals().keys(), globals().values()):
            if zmienna != '__doc__':
                print('\t%20s = %s' % (zmienna, wartosc))

    return silnia


def silnia_rekurencyjnie(n):
    # Zmienne lokalne
    print('\nZmienne lokalne funkcji silnia_iteracyjnie:')
    for zmienna, wartosc in zip(locals().keys(), locals().values()):
        if zmienna != '__doc__':
            print('\t{:>20} = {}'.format(zmienna, wartosc))

    # Zmienne globalne
    print('\nZmienne globalne funkcji silnia_iteracyjnie:')
    for zmienna, wartosc in zip(globals().keys(), globals().values()):
        if zmienna != '__doc__':
            print('\t%20s = %s' % (zmienna, wartosc))

    if n == 0:
        return 1
    return n * silnia_rekurencyjnie(n - 1)


if __name__ == '__main__':
    print('Wynik:', silnia_iteracyjnie(10))
    print('Wynik:', silnia_rekurencyjnie(10))