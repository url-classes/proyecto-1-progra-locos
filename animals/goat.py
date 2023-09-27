from animals.animal import Animal


class Goat(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Queso'
        self.rate_product = 10

    def production(self):
        super().produce_product(self.rate_product)
