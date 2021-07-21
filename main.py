# -*- coding: utf-8 -*-
"""Utilities for writing code that runs on Python 2 and 3"""


def func(arg1, arg2,
         arg3, arg4):
    pass


func(1, 2,
     3, 4)


class Robot:
    """
    Class: Robot!!!
    """

    def __init__(self, name, age) -> object:
        """

        :rtype: object
        """
        self.name = name
        self.age = age

    def hello(self):
        return f'My name is {self.name}'

    def say(self, message):
        return f'{message}'


d = {1: 100, 2: 200}
print(d[1])

r = Robot("qwerty", 84)

print(r.hello())
print(r.say('Hi'))
