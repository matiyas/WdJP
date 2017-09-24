#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Zaimplementuj funkcję vars, która przyjmuje jeden parametr: n i tworzy mienne globalne v1 do
vn o wartościach 1^2, ..., n^2, odpowiednio."""


def vars(n):
    for i in range(1, n + 1):
        globals()['v' + str(i)] = i ** 2


if __name__ == '__main__':
    vars(10)
    for zmienna, wartosc in zip(list(globals().keys()), list(globals().values())):
        print('{} = {}'.format(zmienna, wartosc))
