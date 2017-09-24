#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Napisz program, który na podstawie pliku /etc/passwd wyświetli:
    - nazwy użytkowników
    - wykorzystywane powłoki (podpowiedź: struktura danych set),
    - UID użytkownika nobody,
    - liczbę linii pliku.
"""


if __name__ == '__main__':
    with open('/etc/passwd', 'r') as passwd:
        nazwy_uzytkownikow = []
        powloki = set()
        linie = 0

        for linia in passwd:
            wartosc = linia.split(':')
            nazwy_uzytkownikow.append(wartosc[0])
            powloki.add(wartosc[6].rstrip('\n'))

            if wartosc[0] == 'nobody':
                uid_nobody = wartosc[2]

            linie += 1

        print('Użytkownicy:')
        for uzytkownik in nazwy_uzytkownikow:
            print('\t{}'.format(uzytkownik))

        print('\nPowłoki:')
        for powloka in powloki:
            print('\t{}'.format(powloka))

        print('\nUID użytkownika nobody:', uid_nobody)
        print('\nLiczba linii w pliku:', linie)
