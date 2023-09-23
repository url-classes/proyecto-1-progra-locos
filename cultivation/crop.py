class Crop:
    def __init__(self):
        self.growth_phase = 1
        self.health_lvl = 100
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
        7 > death
            muerte de la planta después de 2 minutos
        '''

    def water_plant(self, amount: int):
        self.health_lvl += 15

    def growth(self, seconds):
        pass

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
