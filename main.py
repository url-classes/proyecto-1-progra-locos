import sys

from main_animals import main_animals
from trading.main_trading import main_trading


def main():
    wallet = 0
    animals_farm: list = []
    inventory_game: list = []

    animals_main = main_animals(animals_farm)

    for i in range(len(animals_main['Animales'])):
        animals_farm.append(animals_main['Animales'][i])

    for i in range(len(animals_main['Inventario'])):
        inventory_game.append(animals_main['Inventario'][i])

    trading_main = main_trading(inventory_game, wallet, animals_farm)

    wallet += trading_main['Wallet']

    print(trading_main['Inventario'])

    inventory_game.clear()
    print(len(trading_main['Inventario']))

    if len(trading_main['Inventario']) == 0:
        pass
    else:
        for i in range(len(trading_main['Inventario'])):
            inventory_game.append(trading_main['Inventario'][i])

    print(inventory_game)
    print('ya')

    sys.exit()


main()

sys.exit()
