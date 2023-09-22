import random


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.hungry = random.randint(75, 90)
        self.health = 100
        self.happiness = random.randint(25, 75)
