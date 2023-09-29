import sys

from main_animals import main_animals
from main_crops import main_crops
from trading.main_trading import main_trading


def main():
    wallet = 0
    animals_farm: list = []
    inventory_animals: list = []
    crops: list = []
    seed_inventory_crops: list = []
    ind_inventory_crops: list = []
    fert_inventory_crops: list = []
    medic_inventory_crops: list = []

    print('MI GRANJA')
    while True:
        print('Bienvenido a tu granja:\n  ' +
              '1 - Cultivar\n  ' +
              '2 - Granja de animales\n  ' +
              '3 - Mi calendario\n  ' +
              '4 - Comercio\n  ' +
              '5 - Salir')
        sel = input('¿A donde deseas ir?: ')

        if sel == '1':
            crops_main = main_crops(crops)
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
            pass

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
