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
            else:
                self.happiness = max(self.happiness - 8, 0)

    def produce_product(self, rate_product: int):
        while self.is_live:
            time.sleep(rate_product)
            self.amount_product = self.amount_product + 1

    def recolect_product(self, product: str):
        diccionario = {'Cantidad': self.productivity * self.amount_product, 'Producto': product}
        self.amount_product = 0
        return diccionario

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

    def __str__(self):
        return self.name
