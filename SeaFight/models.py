# -*- coding: utf-8 -*-

import pickle


class player(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class ship(object):
    def __init__(self, ship_type, coord, one):
        self.ship_type = ship_type
        self.coord = coord
        self.one = one # ореол
        self.hit = [] # счетчик попаданий по кораблю

    def get_state(self):
        return self.__class__

class game_field(object):
    def __init__(self):
        self.field = [0]*100




class Storage(object):
    __obj = None
    players = None

    @classmethod
    def __new__(cls, *args):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
            cls.items = []
        return cls.__obj


