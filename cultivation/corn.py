from crop_product import CropProduct
from crop import Crop


class Corn(Crop):
    def __init__(self):
        super().__init__()
        self.ind_product = CropProduct('Mazorcas', 2, 20.0, True)
        self.seed_product = CropProduct('Semilla de maíz', 1, 12.0, False)



