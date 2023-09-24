class Crop:
    def __init__(self):
        self.__growth_phase = 1
        self.health_lvl = 100
        self.has_plague = False
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

    def water_plant(self):
        self.health_lvl += 15

    def growth(self, seconds):
        change = 60
        level = (100 - self.health_lvl) // 20
        change = change + (10 * level)
        # 60 segundos para subir de fase
        if seconds >= change:
            self.growth_phase += seconds // change

    def __str__(self):
        return f'Estado:\n -Fase de crecimiento: {self.growth_phase}\n ' \
               f'-Nivel de salúd: {self.health_lvl}\n ' \
               f'-Plagas: {self.has_plague}'




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
