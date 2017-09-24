#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from sys import argv


"""Napisz program, który:
    - wyświetla: swoją nazwę, liczbę argumentów, listę wszystkich argumentów
    - pobiera jako parametry dwie liczby, wyświetla ich sumę, różnicę oraz iloczyn,
    - pobiera jako parametry dwie liczby a i b oraz wyświetla 'tak' jeśli a dzieli b, 
      w przeciwnym wypadku wyświetla 'nie'."""


if __name__ == '__main__':
    print('Nazwa:', __file__.split('/')[-1])
    print('Liczba argumentów:', argv.__len__())
    a, b = int(argv[1]), int(argv[2])
    print('{} + {} = {}'.format(a, b, a + b))
    print('{} - {} = {}'.format(a, b, a - b))
    print('{} * {} = {}'.format(a, b, a * b))
    if a % b:
        print('nie')
    else:
        print('tak')


