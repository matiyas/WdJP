#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Jaki będzie wynik wywołania następujących instrukcji? Które z nich są
poprawne i czym się różnią? """


if __name__ == '__main__':
    lista = list(range(10))
    lista1 = list(range(0, -10, -1))
    lista2 = list(range(10, 20, 2))

    print([(x - y) * z for x in lista for y in lista if y > 0 for z in lista
           if z == 4])
    print([(x - y) * z for x in lista for y in lista if y < 0 for z in lista
           if z == 4])
    print([(x - y) * z for x in lista for y in lista for z in lista if y > 0
           and z == 4])
    print([x + y + z for x in lista for y in lista1 if y > 2 for z in lista2
           if z > 0])
    print([x + y + z for x in lista for y in lista1 for z in lista2 if y > 2
           if z > 0])
    print([x + y + z for x in lista for y in lista1 for z in lista2 if y > 2
           and z > 0])
