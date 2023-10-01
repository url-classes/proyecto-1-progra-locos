import sys

from main_animals import main_animals
from main_crops import main_crops
from trading.main_trading import main_trading
from main_calendar import main_calendar, input_timer
from cultivation.medication.fertilizer import Fertilizer
from cultivation.medication.medicine import Medicine
from cultivation.crops.crop_product import CropProduct


def main():
    wallet = 0
    animals_farm: list = []
    inventory_animals: list = []
    crops: list = []
    seed_inventory_crops: list = [
        CropProduct('Semilla de maíz', 3, 12.0, False),
        CropProduct('Semilla de trigo', 3, 20, False),
        CropProduct('Papas de plantación', 3, 36, False),
        CropProduct('Semilla de arroz', 3, 10, False),
        CropProduct('Semilla de algodón', 3, 20.0, False)
    ]
    ind_inventory_crops: list = [
        CropProduct('Mazorcas', 0, 20.0, True),
        CropProduct('Harina', 0, 17.0, True),
        CropProduct('Papas', 0, 36.0, True),
        CropProduct('Arroz', 0, 8.0, True),
        CropProduct('Algodón', 0, 45.0, True)
    ]
    fert_inventory_crops: list = [
        Fertilizer('Fertilizante Nivel 1', 20.0, 4, 180, 10),
        Fertilizer('Fertilizante Nivel 2', 40.0, 2, 1000, 15)
    ]
    medic_inventory_crops: list = [
        Medicine('Medicamento Nivel 1', 45.0, 4, 50, 10),
        Medicine('Medicamento Nivel 2', 90.0, 2, 100, 15)
    ]
    calendar_activities: list[dict] = []

    print('MI GRANJA')
    while True:
        print('Bienvenido a tu granja:\n  ' +
              '1 - Cultivar\n  ' +
              '2 - Granja de animales\n  ' +
              '3 - Mi calendario\n  ' +
              '4 - Comercio\n  ' +
              '5 - Salir')
        sel = input_timer('¿A donde deseas ir?: ', calendar_activities)

        if sel == '1':
            crops_main = main_crops(crops, ind_inventory_crops, seed_inventory_crops, fert_inventory_crops,
                                    medic_inventory_crops)
            crops.extend(crops_main['Cultivos'])
            seed_inventory_crops = crops_main['Productos plantables']
            ind_inventory_crops = crops_main['Productos individuales']
            fert_inventory_crops = crops_main['Fertilizantes']
            medic_inventory_crops = crops_main['Productos medicinales']

        elif sel == '2':
            animals_main = main_animals(animals_farm)
            animals_farm.extend(animals_main['Animales'])
            inventory_animals.extend(animals_main['Inventario'])

            '''for i in range(len(animals_main['Animales'])):
                    animals_farm.append(animals_main['Animales'][i])
    
                for i in range(len(animals_main['Inventario'])):
                    inventory_animals.append(animals_main['Inventario'][i])'''

        elif sel == '3':
            calendar_activities = main_calendar(calendar_activities)

        elif sel == '4':
            trading_main = main_trading(inventory_animals,
                                        wallet, animals_farm,
                                        crops,
                                        seed_inventory_crops,
                                        fert_inventory_crops,
                                        medic_inventory_crops,
                                        ind_inventory_crops)

            wallet += trading_main['Wallet']

            print(wallet)
            if trading_main['type'] == 'animal':
                print(trading_main['Inventario'])
            else:
                seed_inventory_crops = trading_main['Plantables']
                ind_inventory_crops = trading_main['Individuales']
                fert_inventory_crops = trading_main['Fertilizantes']
                medic_inventory_crops = trading_main['Medicamentos']

            '''inventory_animals.clear()
            print(len(trading_main['Inventario']))

            if len(trading_main['Inventario']) == 0:
                pass
            else:
                for i in range(len(trading_main['Inventario'])):
                    inventory_animals.append(trading_main['Inventario'][i])

            print(inventory_animals)
            print('ya')'''
        elif sel == '5':
            sys.exit()


main()

sys.exit()
