# -*- coding: cp1251 -*-
import time


def megadecor(x):
    print "Я хочу " + x + " хлеб"
    
    def whitedecor(func):
        def wrapper():
            print "Белый хлеб"
            func()
            print "Белый хлеб"
        return wrapper

    def blackdecor(func):
        def wrapper():
            print "Черный хлеб"
            func()
            print "Черный хлеб"
        return wrapper

    if (x == "black"):
        return blackdecor
    elif (x == "white"):
        return whitedecor
    else:
        None

@megadecor("white")
def sub():
    print "Колбаса"

sub()
