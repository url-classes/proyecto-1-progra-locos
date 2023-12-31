from animals.animal import Animal


class Bee(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Miel'
        self.rate_product = 13
        self.price_product = 25

    def production(self):
        super().produce_product(self.rate_product)

    def status(self):
        r = super().status_animal(self.product)
        return r

