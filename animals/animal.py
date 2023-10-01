import random
import time


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.is_live = True
        self.hungry = random.randint(75, 90)
        self.health = 100
        self.happiness = random.randint(25, 75)
        self.cleaness = 10
        self.productivity = 1
        self.diseases: list[str] = []
        self.amount_product = 0

    def consume_hunger(self):
        while self.is_live:
            time.sleep(10)
            if self.hungry == 0:
                if 'Hambre' in self.diseases:
                    pass
                else:
                    self.diseases.append('Hambre')
                self.health = max(self.health - 5, 0)
                self.amount_product = max(self.amount_product - 2, 0)
            else:
                self.hungry = max(self.hungry - 10, 0)

    def consume_cleaness(self):
        while self.is_live:
            time.sleep(35)
            if self.cleaness == 0:
                if 'Gripe' in self.diseases:
                    pass
                else:
                    self.diseases.append('Gripe')
                self.health = max(self.health - 7, 0)
                self.amount_product = max(self.amount_product - 2, 0)
            else:
                self.cleaness = max(self.cleaness - 1, 0)

    def consume_happiness(self):
        while self.is_live:
            time.sleep(10)
            if self.happiness == 0:
                if 'Malestar Estomacal' in self.diseases:
                    pass
                else:
                    self.diseases.append('Malestar Estomacal')
                self.health = max(self.health - 1, 0)
                self.amount_product = max(self.amount_product - 2, 0)
            else:
                self.happiness = max(self.happiness - 8, 0)

    def produce_product(self, rate_product: int):
        while self.is_live:
            time.sleep(rate_product)
            self.amount_product = self.amount_product + 1

    def recolect_product(self, product: str, precio: int, inventory: list[dict]):
        diccionario = dict
        product_existence = False

        for item in inventory:
            if product == item['Producto']:
                diccionario = {'Cantidad': item['Cantidad'] + int(self.productivity * self.amount_product),
                               'Producto': product,
                               'Precio': precio}
                inventory.remove(item)
                product_existence = True
                break
        if not product_existence:
            diccionario = {'Cantidad': int(self.productivity * self.amount_product),
                               'Producto': product,
                               'Precio': precio}

        self.amount_product = 0
        inventory.append(diccionario)

    def evalueate(self):
        while True:
            if self.health == 0:
                self.is_live = False

    def stroke(self, time_set: int):
        time.sleep(time_set)
        self.happiness = min(100, self.happiness + 2*time_set)

    def clean(self, time_set: int):
        time.sleep(time_set)
        self.cleaness = min(10, self.cleaness + time_set//13)

    def eat(self, hungry_pts: int):
        self.hungry = min(100, self.hungry + hungry_pts)

    def status_animal(self, product: str):
        r = f'Nombre: {self.name}\nHambre: {self.hungry}\nFelicidad: {self.happiness} Salud: {self.health}\n'
        r += f'Limpieza: {self.cleaness}\nNivel de Productividad: {self.productivity}\nEnfermedades: '
        if len(self.diseases) == 0:
            pass
        else:
            for disease in self.diseases:
                r += f'{disease}, '
        r += f'\nProductos por Recoger: {self.amount_product} {product}'
        return r

    def __str__(self):
        return self.name
