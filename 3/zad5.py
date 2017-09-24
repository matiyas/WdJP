#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Zaimplementuj funkcję factory, która przyjmuje jeden parametr: n i zwraca funję,
która wypisuje na ekranie liczby od 1 do n."""


def factory(n):
    def wypisz():
        i = n - 1
        while i >= 0:
            print(n - i)
            i -= 1
    wypisz()


if __name__ == '__main__':
    factory(10)
