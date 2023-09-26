from animals.animal import Animal


class Goat(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Queso'

    def production(self):
        super().recolect_product(self.product)
