from animals.animal import Animal


class Cow(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.production = 'Leche'
