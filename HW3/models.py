# -*- coding: utf-8 -*-


from utils import get_input_function


class Storage(object):
    obj = None

    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.done = False
        self.type = None # 1-tobuy, 2todo, 3-toread

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToDoItem(BaseItem):
    def __init__(self, heading):
        super(ToDoItem, self).__init__(heading)
        self.type = 2

    def __str__(self):
        return '{} ToDo: {}'.format(
                'Done' if self.done else 'in progress',
                self.heading
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        return ToDoItem(heading)


class ToBuyItem(BaseItem):
    def __init__(self, heading, price):
        super(ToBuyItem, self).__init__(heading)
        self.price = price
        self.type = 1

    def __str__(self):
        return '{} ToBuy: {} for {}'.format(
                'Done' if self.done else 'In progress',
                self.heading,
                self.price,
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price)


class ToReadItem(BaseItem):
    def __init__(self, heading, link, due_date):
        super(ToReadItem, self).__init__(heading)
        self.link = link
        self.due_date = due_date
        self.type = 2

    def __str__(self):
        return '{} ToRead: {} at {} before {}'.format(
                'Done' if self.done else 'In progress',
                self.heading,
                self.link,
                self.due_date
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        link = input_function('Input link: ')
        due_date = input_function('Due date: ')
        return ToReadItem(heading, link, due_date)