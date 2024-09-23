from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class human(Animal):
    def move(self):
        print("I can walk, I can talk")

class Bird(Animal):
    def move(self):
        print("I can fly, I can sing")

class fish(Animal):
    def move(self):
        print("I can swim")

class Ant(Animal):
    def move(self):
        print("I am very small")

h=human()
h.move()

b=Bird()
b.move()

f=fish()
f.move()

a=Ant()
a.move()


