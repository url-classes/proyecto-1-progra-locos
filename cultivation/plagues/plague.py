import math


class Plague:
    def __init__(self):
        self.name = 'Ninguna'
        self.__activity_lvl = 0
        self.damage_streak = 0
        self.frequency = 0

    @property
    def activity_lvl(self):
        return self.__activity_lvl

    @activity_lvl.setter
    def activity_lvl(self, value: int):
        if value >= 100:
            self.__activity_lvl = 100
        elif value <= 0:
            self.__activity_lvl = 0
        else:
            self.__activity_lvl += value

    def __str__(self):
        if self.name == 'Ninguna':
            return self.name
        else:
            return self.name + f' (Nivel de actividad: {self.activity_lvl})'
