

class Cultivos:
    def __init__(self, name: str,
                 product_amount: int,
                 ind_price: float):
        self.product_amount = product_amount
        self.name = name
        self.ind_price = ind_price
        self.growth_phase = 1
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
        self.health_lvl = 100

    def water_plant(self, amount: int):
        self.health_lvl += 15

    def growth(self, seconds):
        pass

    '''
    trigo, maíz, papa, arroz, algodon:
    productos cosechados, cantidad y precio.
    trigo:
	    - 10 libras de harina
	    -  5 kilo de semillas de trigo
    maiz:
	    - 25 elote
	    - 10 kilos semillas de maiz
    papa:
	    - 20 papas
	    - 20 papas como semilla
    arroz:
	    - 10 kilos de arroz
	    - 5 kilos de semilla de arroz
    algodon:
	    - 1 kilo de arroz
	    - 10 kilos semilla de algodon
    '''