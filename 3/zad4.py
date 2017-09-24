#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Zaimplementuj funkję księgowość, która przyjmuje dwa parametry:
stan_konta oraz kwota. Funkja posiada dwie funkje zagnieżdżone: wplata oraz
wyplata, przyjmuje te same dwa paramery: stan_konta oraz kwota. Funkcja
wplata zwraca stan konta po dodaniu do niego kwoty kwota; wyplata zwraca
stan konta po odjęciu niego kwoty kwota. Funkcja ksiegowosc zwraca
symulowane saldo konta dla dwóch przypadków: wpłaty na konto oraz wypłaty z
konta, korzystając z zagnieżdżonych funkcji wplata, wyplata. - Jakie są
zmienne lokalne i globalne funkji ksiegowosc, wplata, wyplata? -
Zaimplementuj funkję wyplata, tak aby wywoływała funkję wplata. Czy ta
modyfikacja wpływa na zmienne lokalne/globalne? - W jaki sposób zmienić
implementację, tak aby funkje wplata, wyplata były wywoływane bez
parametrów? """


def ksiegowosc(stan_konta, kwota):
    # Zmienne lokalne
    print('\nZmienne lokalne funkcji ksiegowosc:')
    for zmienna, wartosc in zip(locals().keys(), locals().values()):
        if zmienna != '__doc__':
            print('\t{:>20} = {}'.format(zmienna, wartosc))

    # Zmienne globalne
    print('\nZmienne globalne funkcji ksiegowosc:')
    for zmienna, wartosc in zip(globals().keys(), globals().values()):
        if zmienna != '__doc__':
            print('\t%20s = %s' % (zmienna, wartosc))

    def wplata():
        # Zmienne lokalne
        print('\nZmienne lokalne funkcji wplata:')
        for zmienna, wartosc in zip(locals().keys(), locals().values()):
            if zmienna != '__doc__':
                print('\t{:>20} = {}'.format(zmienna, wartosc))

        # Zmienne globalne
        print('\nZmienne globalne funkcji wplata:')
        for zmienna, wartosc in zip(globals().keys(), globals().values()):
            if zmienna != '__doc__':
                print('\t%20s = %s' % (zmienna, wartosc))

        print('\nStan konta ({}) po wplacie {}zł: {}.'.format(
            stan_konta, kwota, stan_konta + kwota))

    def wyplata():
        # Zmienne lokalne
        print('\nZmienne lokalne funkcji wyplata:')
        for zmienna, wartosc in zip(locals().keys(), locals().values()):
            if zmienna != '__doc__':
                print('\t{:>20} = {}'.format(zmienna, wartosc))

        # Zmienne globalne
        print('\nZmienne globalne funkcji wyplata:')
        for zmienna, wartosc in zip(globals().keys(), globals().values()):
            if zmienna != '__doc__':
                print('\t%20s = %s' % (zmienna, wartosc))

        wplata()
        print('Stan konta ({}) po wyplacie {}zł: {}.'.format(
            stan_konta, kwota, stan_konta - kwota))

    wyplata()


if __name__ == '__main__':
    ksiegowosc(1000, 450)
