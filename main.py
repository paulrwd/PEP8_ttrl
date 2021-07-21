def func(arg1, arg2,
         arg3, arg4):
    pass


func(1, 2,
     3, 4)


class Robot:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        return f'My name is {self.name}'

    def say(self, message):
        return f'{message}'

r = Robot("qwerty", 84)

print(r.hello())
print(r.say('Hi'))
