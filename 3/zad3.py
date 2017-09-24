#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Zaimplementuj rekurencujnie funkcje FF oraz GG, które zdefiniowano poniżej."""


def FF(n):

    # Zmienne lokalne
    print('\nZmienne lokalne funkcji FF:')
    for zmienna, wartosc in zip(locals().keys(), locals().values()):
        if zmienna != '__doc__':
            print('\t{:>20} = {}'.format(zmienna, wartosc))

    # Zmienne globalne
    print('\nZmienne globalne funkcji FF:')
    for zmienna, wartosc in zip(globals().keys(), globals().values()):
        if zmienna != '__doc__':
            print('\t%20s = %s' % (zmienna, wartosc))

    if n == 0:
        return 2
    return (n + 1) * FF(n - 1)


def GG(n):

    # Zmienne lokalne
    print('\nZmienne lokalne funkcji GG:')
    for zmienna, wartosc in zip(locals().keys(), locals().values()):
        if zmienna != '__doc__':
            print('\t{:>20} = {}'.format(zmienna, wartosc))

    # Zmienne globalne
    print('\nZmienne globalne funkcji GG:')
    for zmienna, wartosc in zip(globals().keys(), globals().values()):
        if zmienna != '__doc__':
            print('\t%20s = %s' % (zmienna, wartosc))

    if n == 0:
        return 3
    if n == 1:
        return 5
    if n == 2:
        return 7
    return GG(n - 3) + (n - 1) * GG(n - 2) + GG(n - 1)


if __name__ == '__main__':
    print(FF(10))
    print(GG(10))