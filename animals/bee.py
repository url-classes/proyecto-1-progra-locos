from animals.animal import Animal


class Bee(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Miel'

    def production(self):
        super().recolect_product(self.product)
