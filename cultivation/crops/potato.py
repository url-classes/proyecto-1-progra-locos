from cultivation.crops.crop import Crop


class Potato(Crop):
    def __init__(self):
        super().__init__()
        self.plant_name = '-Planta de papas-'