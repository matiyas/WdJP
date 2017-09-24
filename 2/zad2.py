#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Zaimplementuj klasę Kolory zawierającą słownik, {...} która jako atrybuty zwraca wartości HEX
odpowiednich kolorów lub AttributeError jeśli kolor nie jest znany."""


class Kolory:
    _kols = {"Silver": "#C0C0C0", "Gray": "#808080", "Black": "#000000", "Red": "#FF0000",
             "Maroon": "#800000", "Yellow": "#FFFF00", "Olive": "#808000", "Lime": "#00FF00",
             "Green": "#008000", "Aqua": "#00FFFF", "Teal": "#008080", "Blue": "#0000FF",
             "Navy": "#000080", "Fuchsia": "#FF00FF", "Purple": "#800080"}

    def __getattr__(self, item):
        kolor = str(item).capitalize()
        if kolor in self._kols.keys():
            return self._kols[kolor]
        raise AttributeError('Nie ma takiego koloru.')

    def __setattr__(self, key, value):
        pass


if __name__ == '__main__':
    print(Kolory().red)
    Kolory().blue = 10
