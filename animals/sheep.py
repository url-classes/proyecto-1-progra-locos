from animals.animal import Animal


class Sheep(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Lana'

    def production(self):
        super().recolect_product(self.product)
