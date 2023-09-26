from animals.animal import Animal


class Chicken(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Huevos'

    def production(self):
        super().recolect_product(self.product)
