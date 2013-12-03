# -*- coding: cp1251 -*-
import time


def megadecor(x):
    print "� ���� " + x + " ����"
    
    def whitedecor(func):
        def wrapper():
            print "����� ����"
            func()
            print "����� ����"
        return wrapper

    def blackdecor(func):
        def wrapper():
            print "������ ����"
            func()
            print "������ ����"
        return wrapper

    if (x == "black"):
        return blackdecor
    elif (x == "white"):
        return whitedecor
    else:
        None

@megadecor("white")
def sub():
    print "�������"

sub()
