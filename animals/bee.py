from animals.animal import Animal



class Bee(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.production = 'Miel'
