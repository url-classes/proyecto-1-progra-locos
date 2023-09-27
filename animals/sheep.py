from animals.animal import Animal


class Sheep(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.product = 'Lana'
        self.rate_product = 20

    def production(self):
        super().produce_product(self.rate_product)
