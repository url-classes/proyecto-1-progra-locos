from animals.animal import Animal


class Chicken(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Huevos'
        self.rate_product = 5

    def production(self):
        super().produce_product(self.rate_product)
