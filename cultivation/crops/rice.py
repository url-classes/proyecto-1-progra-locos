from crop_product import CropProduct
from cultivation.crops.crop import Crop


class Rice(Crop):
    def __init__(self):
        super().__init__()
        self.ind_product = CropProduct('Arroz', 1, 8.0, True)
        self.seed_product = CropProduct('Semilla de arroz', 1, 10, False)
