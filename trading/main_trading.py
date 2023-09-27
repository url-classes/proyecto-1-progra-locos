# from main_crops import main


def sell_item_farm(inventory_animals: list[dict], wallet, animals) -> int:
    find_item = False

    print('Bienvenido a la tienda de la granja, aquí podras vender y comprar productos conforme a la granja.')
    print('OPCIONES:\n' + '1 - Venta de materia prima\n' + '2 - Compra de mejoras granja\n')
    sel_farm = input('Ingresa a la tienda que deseas visitar: ')
    if sel_farm == '1':
        print('Estos son los precios:\n' + 'Huevos c/u = 15 tornillos\n'
              + 'Leche c/u = 100 tornillos \n' + 'Queso c/u = 200 tornillos\n' + 'Lana c/u = 50 tornillos\n'
              + 'Miel c/u = 25 tornillos\n')

        for item in inventory_animals:
            print(f"Tienes {item['Cantidad']}x {item['Producto']}.")

        sell_item = input('¿Qué deseas vender?: ')
        for item in inventory_animals:
            if sell_item == item['Producto']:
                find_item = True
                sell_item = item
        amount_sell_item = int(input('¿Cuántas unidades deseas vender? '))
        if find_item:
            if sell_item['Cantidad'] - amount_sell_item >= 0:
                if sell_item['Cantidad'] - amount_sell_item == 0:
                    inventory_animals.remove(sell_item)
                    coins_add = sell_item['Cantidad'] * sell_item['Precio']
                else:
                    coins_add = (sell_item['Cantidad'] - amount_sell_item) * sell_item['Precio']
            else:
                print('No puedes vender esa cantidad de objetos.')
                return sell_item_farm(inventory_animals, wallet, animals)
        else:
            print('Vaya ese item, no lo encontré.')
            return sell_item_farm(inventory_animals, wallet, animals)
        return coins_add

    elif sel_farm == '2':
        print('Estos son los precios:\n' + '1x Mejora de productividad = 600 tornillos\n')
        if wallet - 600 >= 0:
            coins_remove = -600
            for animal in animals:
                animal.productivity += 1
            return coins_remove
        else:
            print('Parece, que no puedes completar esta compra de productividad.')


def main_trading(inventory_animals: list[dict], wallet: int, animals):
    print('COMPRA Y VENTA')
    print('Bienvenido a la sección de compra y venta de productos.')
    print('OPCIONES:\n  ' +
          '1 - Productos de cultivo\n  ' +
          '2 - Productos de la granja de animales\n  ')
    sel = input('Ingrese la sección a la que deseas ingresar: ')
    if sel == '1':
        # cultivos
        pass
    elif sel == '2':
        wallet += sell_item_farm(inventory_animals, wallet, animals)
    return {'Wallet': wallet, 'Inventario': inventory_animals}
