import time
import sys

class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots
    def eat_leaves_from_trees(self):
        print('eating leaves')
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

reginald = Giraffes()

def this_is_a_normal_function():
    print('I am a normal function')

class ThisIsMySillyClass:
    def this_is_a_class_function():
        print('I am a class function.')
    def this_is_also_a_class_function():
        print('I am also a class function. See?')