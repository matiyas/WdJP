#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Napisz program, który prosi użykownika o wymiślenie liczby całkowitej z przedziału 1 - 30,
a następnie stara się odgadnąć tę liczbę. Jeśli liczba wskazana przez program była błędna to
program pyta czy liczba użytkonika jest mniejsza czy większa od podanej i wykorzystuje tę
informację przy kolejnej próbie."""

if __name__ == '__main__':
    input('Wymyśl liczbę całkowitą z przedziału 1 - 30. Wciśnij dowolny klawisz, aby kontynuować.')

    zakres = {'min': 2
        , 'max': 30}
    while True:
        liczba = (zakres['min'] + zakres['max']) // 2
        if zakres['min'] >= zakres['max'] or \
                input('Czy ta liczba to {}? [y/N] '.format(liczba)) == 'y':
            print('Wymyślona przez Ciebie liczba to', liczba, '.')
            break
        else:
            if input('Czy ta liczba jest większa niż {}? [y/N] '.format(liczba)) == 'y':
                zakres['min'] = liczba + 1
            else:
                zakres['max'] = liczba - 1
