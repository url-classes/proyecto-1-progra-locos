from animals.animal import Animal


class Goat(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Queso'
        self.rate_product = 40
        self.price_product = 200

    def production(self):
        super().produce_product(self.rate_product)

    def status(self):
        r = super().status_animal(self.product)
        return r
