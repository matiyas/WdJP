#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Zaimplementuj własną klasę liczb zespolonych. Zaimplementuj w niej metodę
pozwalającą na zwiększanie wartości o liczbę całkowitą, rzeczywistą oraz
zespoliną (własnej klasy). """


class MojaZespolona:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, MojaZespolona):
            return MojaZespolona(self.real + other.real,
                                 self.imag + other.imag)
        if isinstance(other, float) or isinstance(other, int):
            return MojaZespolona(self.real + other, self.imag)

    def __radd__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return MojaZespolona(self.real + other, self.imag)

    def __iadd__(self, other):
        if isinstance(other, MojaZespolona):
            self.real += other.imag
            self.imag += other.imag
            return self
        if isinstance(other, float) or isinstance(other, int):
            self.real += other
            return self

    def __str__(self):
        return '{} + {}i'.format(self.real, self.imag)


if __name__ == '__main__':
    z1 = MojaZespolona(3, 4)
    z2 = MojaZespolona(2, 5)
    print(z1 + z2)
    print(z1 + 10)
    print(10 + z2)
    z1 += 10
    print(z1)
