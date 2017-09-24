#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    """Program pobiera od uzytkownika dwie dodatnie liczby całkowite n i m, i wypisuje w
        kolejnych wierszach wszystkie dodatnie wielokrotności n mniejsze od m."""

    n, m = map(int, input("Podaj dwie liczby całkowite oddzielone spacją: ").split())

    for i in range(1, m // n + 1):
        print(n * i)
