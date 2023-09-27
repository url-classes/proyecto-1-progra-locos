from animals.animal import Animal


class Cow(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Leche'
        self.rate_product = 30
        self.price_product = 100

    def production(self):
        super().produce_product(self.rate_product)

    def status(self):
        r = super().status_animal(self.product)
        return r
