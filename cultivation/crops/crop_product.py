class CropProduct:
    def __init__(self, name: str,
                 amount: float,
                 price: float,
                 category: bool):
        self.name = name
        self.amount = amount
        # cantidad en libras
        self.price = price
        self.category = category
        '''
        categorías:
            - producto consumible : True
            - producto de plantación : False 
        '''