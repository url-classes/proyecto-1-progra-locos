from cultivation.crops.crop import Crop


class Rice(Crop):
    def __init__(self):
        super().__init__()
        self.plant_name = '-Planta de arroz-'
