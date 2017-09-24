#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


"""Zaimplementuj klasę LiczbaLosowa, która nie umożliwia tworzenia atrybutów, a w przypadku próby 
odczytu zwraca liczbę losową."""


class LiczbaLosowa:
    def __setattr__(self, key, value):
        pass

    def __getattr__(self, item):
        return randint(-2**32, 2**32)


if __name__ == '__main__':
    ll = LiczbaLosowa()
    ll.cos = 10
    print(ll.cos)
