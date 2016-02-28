# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import inspect
import json

# import custom_exceptions
from custom_exceptions import UserExitException
from models import BaseItem
from utils import get_input_function
import pickle

__author__ = 'sobolevn'


class BaseCommand(object):
    def __init__(self, command):
        self._command = command

    @property
    def command(self):
        return self._command

    @staticmethod
    def label():
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        raise NotImplemented()


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():

        def class_filter(klass):
            return inspect.isclass(klass) \
                   and klass.__module__ == BaseItem.__module__ \
                   and issubclass(klass, BaseItem) \
                   and klass is not BaseItem

        classes = inspect.getmembers(
            sys.modules[BaseItem.__module__],
            class_filter,
        )
        return dict(classes)

    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{}: {}'.format(index, name))

        input_function = get_input_function()
        selection = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                break
            except ValueError:
                print('Bad input, try again.')

        selected_key = list(classes.keys())[selection]
        selected_class = classes[selected_key]
        print('Selected: {}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct()

        objects.append(new_object)
        print('Added {}'.format(str(new_object)))
        print()
        return new_object


class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')


class DoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'done'

    def perform(self, objects, *args, **kwargs):
        try:
            index = int(input('Input index of task: '))
            objects[index].done = True
            print('Tusk %s is finished' % index)
        except IndexError:
            print('Нет такой записи!')


class SortCommand(BaseCommand):
    @staticmethod
    def label():
        return 'sort'

    def perform(self, objects, *args, **kwargs):
        z = int(input('how to sort? 1 - in progress/done, 2 - by type: '))

        if z == 1:
            objects.sort(key=lambda x: x.done)
        elif z == 2:
            objects.sort(key=lambda x: x.type)
        else:
            print('try again')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class UndoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'undone'

    def perform(self, objects, *args, **kwargs):
        try:
            index = int(input('Input index of task: '))
            objects[index].done = False
            print('Tusk %s in progress again' % index)
        except IndexError:
            print('Нет такой записи!')


class SaveCommand(BaseCommand):
    @staticmethod
    def label():
        return 'save'

    def perform(self, objects, *args, **kwargs):
        #fts = open('todolist.txt', 'wb')
        #for i in range(len(objects)):
        #    print(objects[i], file=fts)
        #print('all tasks save to todolist.txt')
        #fts.close()

        pickle.dump(objects, open("ToDoList.txt", 'wb'))
        print('all tasks save to ToDoList.txt')


class LoadCommand(BaseCommand):
    @staticmethod
    def label():
        return 'load'

    def perform(self, objects, *args, **kwargs):
        try:
            fto = open("ToDoList.txt",'rb')
            ftot = pickle.load(fto)
            for i in ftot:
                objects.append(i)
            print("All tasks upload from ToDoList.txt\n"
                  "you can type 'list' to watch it")
        except IOError:
            print("File does not exist")

        #for i in range(len(objects)):
        #    objects[i]=temp[i]
        #    print(objects[i])


