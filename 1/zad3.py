#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import factorial


if __name__ == '__main__':
    """Oblicz sumę cyfr liczby 100!."""
    print(sum(map(int, list(str(factorial(10))))))
