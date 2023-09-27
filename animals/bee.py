from animals.animal import Animal


class Bee(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Miel'
        self.rate_product = 13

    def production(self):
        super().produce_product(self.rate_product)
