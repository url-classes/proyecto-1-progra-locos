import random
import math
from cultivation.plagues.aphid import Aphid
from cultivation.plagues.caterpillar import Caterpillar
from cultivation.plagues.tripp import Tripp
from cultivation.plagues.plague import Plague


class Crop:
    def __init__(self):
        self.__growth_phase = 0
        self.__health_lvl = 100
        self.actual_plague = Plague()
        self.__change = 60
        self.lifespan = 1 # minutos
        self.productivity = 1

    @property
    def change(self):
        return self.__change

    @change.setter
    def change(self, value):
        if value <= 60:
            self.__change = 60
        else:
            self.__change = value

    @property
    def growth_phase(self):
        if self.__growth_phase == 1:
            return f'Brotando (Nivel {self.__growth_phase})'
        elif 2 <= self.__growth_phase < 3:
            return f'Creciendo (Nivel {self.__growth_phase})'
        else:
            return f'Madura'

    @growth_phase.setter
    def growth_phase(self, value):
        self.__growth_phase = value

    @property
    def health_lvl(self) -> int:
        return self.__health_lvl

    @health_lvl.setter
    def health_lvl(self, value: int):
        if value <= 0:
            self.__health_lvl = 0

        elif value >= 100:
            self.__health_lvl = 100

        else:
            self.__health_lvl = value

    def water_plant(self):
        self.health_lvl += 15
        self.change -= 30

    def growth(self):
        level = (100 - self.health_lvl) // 20
        self.change = self.change + (10 * level)
        if self.lifespan >= self.change // 60:
            self.__growth_phase = self.lifespan // (self.change // 60)

    def set_lifespan(self, seconds):
        self.lifespan += round(seconds / 60, 1)

    def plague_attack(self, seconds):
        self.health_lvl -= self.actual_plague.damage_streak
        self.health_lvl -= math.trunc(seconds)
        if self.actual_plague.activity_lvl == 0:
            self.actual_plague = Plague()

    def get_sick(self, seconds):
        if self.actual_plague.name == 'Ninguna':
            plague_index = random.randint(1, 3)
            plagues = {
                1: Aphid(),
                2: Caterpillar(),
                3: Tripp()
            }
            if int(round(self.lifespan)) == \
                    random.randint(int(round(self.lifespan)),
                                   int(round(self.lifespan)) + plagues[plague_index].frequency):

                self.actual_plague = plagues[plague_index]

    def fertilize(self, fertilizer):
        self.change -= fertilizer.change_delta
        self.health_lvl += fertilizer.health_delta

    def medic(self, medicine):
        self.actual_plague.activity_lvl -= medicine.plague_activity_change
        self.health_lvl += medicine.plant_health_increment
        if self.actual_plague.activity_lvl == 0:
            self.actual_plague = Plague()

    def __str__(self):
        return f'Estado:\n -Fase de crecimiento: {self.growth_phase}\n ' \
               f'-Nivel de salúd: {self.health_lvl}\n ' \
               f'-Plagas: {str(self.actual_plague)}\n ' \
               f'-Tiempo para cambiar de fase: {round(self.change / 60, 1)} minutos\n ' \
               f'-Tiempo de vida: {round(self.lifespan - 1, 1) } minutos'
