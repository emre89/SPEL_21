import random

class Dealer:
    def __init__(self):
        self.total = 0

    def play(self):
        rolls = []
        while self.total < 17:
            value = random.randint(1, 6)
            self.total += value
            rolls.append(value)
        return rolls

    def reset(self):
        self.total = 0
