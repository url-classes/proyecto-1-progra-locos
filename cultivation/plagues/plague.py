import random


class Plague:
    def __init__(self):
        self.name = 'Ninguna'
        self.__activity_lvl = 100
        self.damage_streak = 0
        self.frequency = 0

    @property
    def activity_lvl(self):
        return self.__activity_lvl

    @activity_lvl.setter
    def activity_lvl(self, value: int):
        if self.__activity_lvl + value >= 100:
            self.__activity_lvl = 100
        else:
            self.__activity_lvl += value

    def set_performance(self, seconds):
        self.activity_lvl += 2

    def __str__(self):
        return self.name
