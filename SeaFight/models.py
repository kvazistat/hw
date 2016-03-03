# -*- coding: utf-8 -*-

import pickle

class player(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Ship(object):
    def __init__(self, ship_type, x, y, v_or_h):
        self.ship_type = ship_type
        self.x = x
        self.y = y
        self.v_or_h = v_or_h
        self.hit = [] # счетчик попаданий по кораблю

    def set_ship(self, field, n):
        if self.ship_type == n and self.v_or_h == 'h':
            for i in range(self.x, self.x + n):
                field[self.x][i] = 'O'
        elif self.ship_type == n and self.v_or_h == 'v':
            for i in range(self.x, self.x + n):
                field[i][self.y] = 'O'
        return field


class GameField(object):
    def __init__(self):
        self.field = [0]*12
        self.field[0]=[' ','1','2','3','4','5','6','7','8','9','10']
        for i in range(1,11):
            self.field[i] = ['s']*11
        for j in range(1,11):
            self.field[j][0] = str(j)


