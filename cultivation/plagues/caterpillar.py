from cultivation.plagues.plague import Plague


class Caterpillar(Plague):
    def __init__(self):
        super().__init__()
        self.frequency = 20
        self.activity_lvl = 100
        self.damage_streak = 10
        self.name = 'Orugas'
