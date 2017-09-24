#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import arange
from itertools import product


"""Zaimplementuj fraktal przedstawiający dywan Sierpińskiego."""


class Kwadrat:
    def __init__(self, p1, p2):
        self.p1 = [0, 0]
        self.p2 = [0, 0]

        if p1[0] < p2[0]:
            self.p1[0] = p1[0]
            self.p2[0] = p2[0]
        else:
            self.p1[0] = p2[0]
            self.p2[0] = p1[0]

        if p1[1] < p2[1]:
            self.p1[1] = p1[1]
            self.p2[1] = p2[1]
        else:
            self.p1[1] = p2[1]
            self.p2[1] = p1[1]

    def podziel(self):
        step = abs(self.p1[0] - self.p2[0]) / 3
        p = list(product(arange(self.p1[0], self.p2[0]+1, step),
                         arange(self.p1[1], self.p2[1]+1, step)))
        return [Kwadrat(p[x], p[x+5]) for x in range(11)
                if (x+1) % 4 != 0 and x != 5]

    def __str__(self):
        return r'<polygon points="{},{} {},{} {},{} {},{}" ' \
               r'style="fill:black;"/>'.format(self.p1[0], self.p1[1],
                                               self.p2[0], self.p1[1],
                                               self.p2[0], self.p2[1],
                                               self.p1[0], self.p2[1])


def list_to_svg(kwadraty):
    res = '''<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n'''
    res += "\n".join([str(x) for x in kwadraty])
    return res + '</svg>'


if __name__ == '__main__':
    kwadraty = [Kwadrat([1, 1], [700, 700])]
    for _ in range(4):
        nowe = []
        for k in kwadraty:
            nowe += k.podziel()
        kwadraty = nowe

    with open('dywan.svg', 'w') as dywan:
        dywan.write(list_to_svg(kwadraty))
