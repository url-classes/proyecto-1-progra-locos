from animals.animal import Animal


class Cow(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Leche'
        self.rate_product = 30

    def production(self):
        super().produce_product(self.rate_product)

