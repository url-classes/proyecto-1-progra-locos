import random
from cultivation.plagues.aphid import Aphid
from cultivation.plagues.caterpillar import Caterpillar
from cultivation.plagues.tripp import Tripp
from cultivation.plagues.plague import Plague


class Crop:
    def __init__(self):
        self.__growth_phase = 1
        self.__health_lvl = 100
        self.actual_plague = Plague()
        self.change = 60
        self.lifespan = 0 # minutos
        '''
        phases:
        > outbreak (30 sec per state)
           1 - outbreak state 1 
           2 - outbreak state 1
        > growth (20 sec per state)
           3 - growth state 1 
           4 - growth state 2
           5 - growth state 3
        6 > mellowing (120 sec)
        '''

    @property
    def growth_phase(self):
        if self.__growth_phase == 1 or self.__growth_phase == 2:
            return f'Brotando (Nivel {self.__growth_phase})'
        elif 3 <= self.__growth_phase < 6:
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

    def water_plant(self):
        self.health_lvl += 15

    def growth(self, seconds):
        level = (100 - self.health_lvl) // 5 # cuantos 20s hay en la salud de la planta
        self.change = self.change + (10 * level)
        # 60 segundos para subir de fase
        if seconds >= self.change:
            self.growth_phase += seconds // self.change
        self.lifespan += round(seconds / 60, 1)
        self.health_lvl -= self.actual_plague.damage_streak
        if self.actual_plague.activity_lvl != 100:
            self.actual_plague.activity_lvl += 5
        '''pendiente: cambios a la salud de una plaga (opcional)'''
        self.health_lvl -= 2 * (seconds // 2)
        if self.actual_plague.activity_lvl == 0:
            self.actual_plague = Plague()

    def __str__(self):
        return f'Estado:\n -Fase de crecimiento: {self.growth_phase}\n ' \
               f'-Nivel de salúd: {self.health_lvl}\n ' \
               f'-Plagas: {str(self.actual_plague)}\n ' \
               f'-Tiempo para cambiar de fase: {round(self.change / 60, 2)} minutos\n ' \
               f'-Tiempo de vida: {round(self.lifespan, 1)} minutos'

    def get_sick(self, seconds):
        if self.actual_plague == 'Ninguna':
            if round(self.lifespan) % random.randint(1, 12) == 0:
                plague_index = random.randint(1, 3)
                plagues = {
                    1: Aphid(),
                    2: Caterpillar(),
                    3: Tripp()
                }
                self.actual_plague = plagues[plague_index]

    '''
    trigo, maíz, papa, arroz, algodon:
    productos cosechados, cantidad y precio.
    trigo:
	- 10 libras de harina Q70.00
	- 5 kilo de semillas de trigo  Q150.00
    maiz:
	- 25 elote Q45.00
	- 10 kilos semillas de maiz Q35.00
    papa:
	- 20 papas Q100.00
	- 20 papas como semilla Q100.00
    arroz:
	- 10 kilos de arroz Q500.00
	- 5 kilos de semilla de arroz Q250.00
    algodon:
	- 1 kilo de algodon puro Q600.00
	- 10 kilos semilla de algodon Q450.00
    '''
