class Cultivos:
    def __init__(self, name: str, health_lvl: int, amount: int, products: []):
        self.products = products
        self.name = name
        self.amount = amount
        self.growth_phase = 'outbreak'
        self.health_lvl = health_lvl


