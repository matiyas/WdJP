#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    """Oblicz różnicę między kwadratem sumy a sumą kwadratów pierwszych stu liczb naturalnych."""
    print(sum(range(1, 101)) ** 2 - sum(map(lambda x: x ** 2, range(1, 101))))
