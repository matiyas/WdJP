#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Zaimplementuj na dwa sposoby (rekurencyjnie oraz iteracyjnie) funkcję
suma obliczającą sumę kolejnych liczb naturanlych od 0 do liczby podanej
jako parametr wywołania funkcji. Funkcje powinny wypisywać (w czytelny i
zrozumiały sposób) na ekran tablicę zmiennych lokalnych oraz globalnych. - W
jaki sposób zmieniają się zmienne lokalne i globalne w zależności od sposobu
implementacji (rekurencja kontra iteracja)? - Czy można zaimplementować
iteracyjnie funkcję suma w 2 liniach kodu? """


def suma_iteracyjnie(n):
    suma = 0
    for x in range(1, n+1):
        suma += x

    # Zmienne lokalne
    print('\nZmienne lokalne funkcji suma_iteracyjnie:')
    for zmienna, wartosc in zip(locals().keys(), locals().values()):
        if zmienna != '__doc__':
            print('\t{:>20} = {}'.format(zmienna, wartosc))

    # Zmienne globalne
    print('\nZmienne globalne funkcji suma_iteracyjnie:')
    for zmienna, wartosc in zip(globals().keys(), globals().values()):
        if zmienna != '__doc__':
            print('\t%20s = %s' % (zmienna, wartosc))
    return suma


def suma_rekurencyjnie(n):
    if n == 0:
        # Zmienne lokalne
        print('\nZmienne lokalne funkcji suma_rekurencyjnie:')
        for zmienna, wartosc in zip(locals().keys(), locals().values()):
            if zmienna != '__doc__':
                print('\t%20s = %s' % (zmienna, wartosc))

        # Zmienne globalne
        print('\nZmienne globalne funkcji suma_rekurencyjnie:')
        for zmienna, wartosc in zip(globals().keys(), globals().values()):
            if zmienna != '__doc__':
                print('\t%20s = %s' % (zmienna, wartosc))
        return 0
    return n + suma_rekurencyjnie(n - 1)


if __name__ == '__main__':
    n = 10
    print(suma_iteracyjnie(n))
    print(suma_rekurencyjnie(n))
    print(sum(range(n + 1)))
