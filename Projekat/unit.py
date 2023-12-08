from constants import *
import random

class Unit():
    def __init__(self, items):
        self.value = 0
        self.weight = 0
        self.items = items
        self.calculate_value()
    def calculate_value(self):
        for i, item in enumerate(self.items):
            if item == 1:
                self.value += ITEMS[i][1]
                self.weight += ITEMS[i][0]
        if self.weight > CAPACITY:
            self.value = 0
        #self.value *= random.random()