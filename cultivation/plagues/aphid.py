from cultivation.plagues.plague import Plague


class Aphid(Plague):
    def __init__(self):
        super().__init__()
        self.frequency = 5
        self.activity_lvl = 50
        self.damage_streak = 5
        self.name = 'Pulgónes'
