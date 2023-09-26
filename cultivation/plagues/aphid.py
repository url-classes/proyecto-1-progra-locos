from cultivation.plagues.plague import Plague


class Aphid(Plague):
    def __init__(self):
        super().__init__()
        self.frequency = 120
        # frecuencia en minutos de aparecer
        self.damage_streak = 10
        # +10 de daño a cada cierto tiempo
        self.name = 'Pulgónes'
