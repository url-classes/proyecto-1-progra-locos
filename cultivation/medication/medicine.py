class Medicine:
    def __init__(self, name: str,
                 price: float,
                 amount: int,
                 plague_activity_change: int,
                 plant_health_increment: int):
        self.name = name
        self.price = price
        self.amount = amount
        self.plague_activity_change = plague_activity_change
        self.plant_health_increment = plant_health_increment

    def __str__(self):
        return f'{self.name}:\n  ' \
               f'-Precio: {self.price}\n  ' \
               f'-Cantidad disponible: {self.amount}\n  ' \
               f'-Daño a una plaga: -{self.plague_activity_change} de daño\n  ' \
               f'-Salúd proporcionada a una planta: +{self.plant_health_increment}'
