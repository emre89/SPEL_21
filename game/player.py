import random

class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def roll(self):
        value = random.randint(1, 6)
        self.total += value
        return value

    def reset(self):
        self.total = 0
