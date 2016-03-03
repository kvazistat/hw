# -*- coding: utf-8 -*-

import random
from models import *
from commands import *


def cr_ship(ship_type, x, y, v_or_h):  # создание кораблей
    x = Ship(ship_type, x, y, v_or_h)
    return x


def set_ship(ship, field):
    return field

def print_field(field):
    for i in range(11):
        print(field[i])


def main():
    count = []
    field = GameField().field
    en_field = GameField().field
    print_field(field)
    #pl1 = input('please, enter your name: ')
    #print('%s versus %s' % (player(pl1), player('MegaMozg9000')))
    n = int(input('skoka palub? '))
    for i in range(5-n):
        x = int(input('coord x? '))
        y = int(input('coord y? '))
        h = input('or? ')
        if h == 'v' or h =='h':
            z = Ship(int(n),x,y,h)
            field = Ship.set_ship(z, field, z.ship_type)
            print_field(field)
        else:
            i -= 1
        #тут корочи вписать обработчик эксепта по типу кораблей

main()