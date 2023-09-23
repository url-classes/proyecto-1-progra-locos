from crop_product import CropProduct
from cultivation.crops.crop import Crop


class Wheat(Crop):
    def __init__(self):
        super().__init__()
        self.ind_product = CropProduct('Harina', 2, 17.0, True)
        self.seed_product = CropProduct('Semilla de trigo', 1, 20, False)