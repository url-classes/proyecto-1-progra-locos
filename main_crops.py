from cultivation.crops.corn import Corn
from cultivation.crops.cotton import Cotton
from cultivation.crops.potato import Potato
from cultivation.crops.rice import Rice
from cultivation.crops.wheat import Wheat

from cultivation.crops.crop_product import CropProduct

from cultivation.plagues.aphid import Aphid
from cultivation.plagues.caterpillar import Caterpillar
from cultivation.plagues.tripp import Tripp

crops: list[Corn | Cotton | Potato | Rice | Wheat] = []
plagues: list[Aphid | Caterpillar | Tripp] = []
products: list[CropProduct] = [
    CropProduct('Semilla de maíz', 10, 12.0, False),
    CropProduct('Semilla de trigo', 10, 20, False),
    CropProduct('Papas de plantación', 24, 36, False),
    CropProduct('Semilla de arroz', 10, 10, False),
    CropProduct('Semilla de algodón', 10, 20.0, False)
] 


def add_crop():
    print('ELIGE UN CULTIVO: ')


def rinse():
    pass


def collect():
    pass


def fertilize():
    pass


def medic():
    pass


def crop_stats():
    pass


def crop_product_stats():
    pass


def main():
    print('---Sistema de Cultivos---')
    print('¿QUE QUIERES HACER?:\n 1 - Agregar un cultivo\n ' +
          '2 - Ver el estado de tus cultivos\n ' +
          '3 - Regar mis cultivos\n ' +
          '4 - Recolectar cosechas\n ' +
          '5 - Fertilizar la tierra\n ' +
          '6 - Medicar un cultivo\n ' +
          '7 - Revisar mis productos de cultivo')

    sel = input(': ')
    if sel == '1':
        add_crop()
    elif sel == '2':
        crop_stats()
    elif sel == '3':
        rinse()
    elif sel == '4':
        collect()
    elif sel == '5':
        fertilize()
    elif sel == '6':
        medic()
    elif sel == '7':
        crop_product_stats()


main()
