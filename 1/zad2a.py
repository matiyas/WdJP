#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    """Program pobiera od użytkownika nieujemną liczbę całkowitą n i oblicza sumę kwadratów liczb od
       0 do n. """

    print('Wynik:', sum(map(lambda a: a ** 2, range(int(input('Podaj liczbę nieujemną liczbę '
                                                              'całkowitą: ')) + 1))))
