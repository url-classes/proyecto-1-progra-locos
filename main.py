import sys

from main_animals import main_animals
from main_crops import main
from trading.main_trading import main_trading


def main():
    wallet = 0
    animals_farm: list = []
    inventory_animals: list = []
    seed_inventory_crops: list = []
    ind_inventory_crops: list = []
    fert_inventory_crops: list = []
    medic_inventory_crops: list = []

    animals_main = main_animals(animals_farm)

    for i in range(len(animals_main['Animales'])):
        animals_farm.append(animals_main['Animales'][i])

    for i in range(len(animals_main['Inventario'])):
        inventory_animals.append(animals_main['Inventario'][i])

    trading_main = main_trading(inventory_animals, wallet, animals_farm)

    wallet += trading_main['Wallet']

    print(trading_main['Inventario'])

    inventory_animals.clear()
    print(len(trading_main['Inventario']))

    if len(trading_main['Inventario']) == 0:
        pass
    else:
        for i in range(len(trading_main['Inventario'])):
            inventory_animals.append(trading_main['Inventario'][i])

    print(inventory_animals)
    print('ya')



    sys.exit()


main()

sys.exit()
