##class MyClass:
##    """A simple example class"""
##    i = 12345
##
##    def f(self):
##        return 'hello world'
##
##print(MyClass.i)
##print(MyClass.f)
##
##x=MyClass()
##
##print(x.i)
##print(x.f)

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
