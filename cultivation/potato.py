from crop_product import CropProduct
from crop import Crop


class Potato(Crop):
    def __init__(self):
        super().__init__()
        self.ind_product = CropProduct('Papas', 3.0, 36.0, True)
        self.seed_product = CropProduct('Papas de plantación', 3.0, 36, False)