class Fertilizer:
    def __init__(self, name: str,
                 price: float,
                 amount: int,
                 change_delta: int,
                 health_delta: int):
        self.name = name
        self.price = price
        self.amount = amount
        self.change_delta = change_delta
        self.health_delta = health_delta

    def __str__(self):
        return f'{self.name}:\n  ' \
               f'-Precio: {self.price}\n  ' \
               f'-Cantidad disponible: {self.amount}\n  ' \
               f'-Beneficio de crecimiento: -{self.change_delta} segundos de tardanza\n  ' \
               f'-Salúd proporcionada a una planta: +{self.health_delta}'
