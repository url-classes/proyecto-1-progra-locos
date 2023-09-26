from animals.animal import Animal


class Cow(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Leche'

    def production(self):
        super().recolect_product(self.product)

