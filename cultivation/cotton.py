from crop_product import CropProduct
from crop import Crop


class Cotton(Crop):
    def __init__(self):
        super().__init__()
        self.ind_product = CropProduct('Algodón', 0.5, 45.0, True)
        self.seed_product = CropProduct('Semilla de algodón', 1, 20.0, False)