#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Napisz program, który pobiera od użytkownika liczbę całkowitą n i wyświetla na ekranie
wartości funkcji FF(n) oraz GG(n)."""


def FF(n):
    if n == 0:
        return 2

    return (n + 1) * FF(n - 1)


def GG(n):
    if n == 0:
        return 3
    if n == 1:
        return 5
    if n == 2:
        return 7

    return GG(n - 3) + (n - 1) * GG(n - 2) + GG(n - 1)


if __name__ == '__main__':
    n = int(input('Podaj liczbę całkowitą: '))
    print('FF({}) = {}'.format(n, FF(n)))
    print('GG({}) = {}'.format(n, GG(n)))
