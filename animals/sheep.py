from animals.animal import Animal


class Sheep(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Lana'
        self.rate_product = 20
        self.price_product = 50

    def production(self):
        super().produce_product(self.rate_product)

    def status(self):
        r = super().status_animal(self.product)
        return r
