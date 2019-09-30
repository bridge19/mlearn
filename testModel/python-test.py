#!/usr/bin/python
# -*- coding: UTF-8 -*-


def outer():
    num = 10

    def inner():
        num = 100
        print(num)
    inner()
    print(num)


outer()
