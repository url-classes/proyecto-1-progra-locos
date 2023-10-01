# from main_crops import main
from main_crops import main_crops, general_show_function
from cultivation.crops.crop_product import CropProduct
from cultivation.crops.crop import Crop
from cultivation.medication.fertilizer import Fertilizer
from cultivation.medication.medicine import Medicine

buy_medic: list[Medicine] = [
    Medicine('Medicamento Nivel 1', 45.0, 20, 50, 10),
    Medicine('Medicamento Nivel 2', 90.0, 20, 100, 15)
]

buy_fert: list[Fertilizer] = [
    Fertilizer('Fertilizante Nivel 1', 20.0, 20, 180, 10),
    Fertilizer('Fertilizante Nivel 2', 40.0, 20, 1000, 15)
]

buy_seed: list[CropProduct] = [
    CropProduct('Semilla de maíz', 10, 12.0, False),
    CropProduct('Semilla de trigo', 10, 20, False),
    CropProduct('Papas de plantación', 10, 36, False),
    CropProduct('Semilla de arroz', 10, 10, False),
    CropProduct('Semilla de algodón', 10, 20.0, False)
]


def show_crop_products_sellable(ind_products, seed_products):
    print('TU INVENTARIO')
    general_show_function(ind_products, 'Productos consumibles')
    general_show_function(seed_products, 'Productos plantables')


def show_crop_products_buyable(fertilizers, medic_products):
    general_show_function(fertilizers, 'Fertilizantes (solo compra)')
    general_show_function(medic_products, 'Medicamentos (solo compra)')


def buy(buy_list, title: str, wallet: int, inv_list):
    general_show_function(buy_list, title)
    sel3 = int(input('Ingresa el producto que quieres comprar: ')) - 1
    cant = int(input('Ingresa la cantidad del producto a comprar: '))
    if buy_list[sel3].amount - cant <= 0:
        print('No hay suficientes productos de este tipo en venta.')
    else:
        if wallet - buy_list[sel3].price < 0:
            print('No tienes suficiente dinero para comprar este objeto')
            return 0
        else:
            remove_wallet = buy_list[sel3].price * cant
            buy_list[sel3].amount -= cant
            inv_list[sel3].amount += cant
            return remove_wallet


def sell(inv_list, title):
    general_show_function(inv_list, title)
    sel3 = int(input('Ingresa el producto que quieres vender: ')) - 1
    cant = int(input('Ingresa la cantidad del producto a vender: '))
    if inv_list[sel3].amount - cant < 0:
        print('No puedes vender este producto en esta cantidad')
        return 0
    else:
        inv_list[sel3].amount -= cant
        increase_wallet = inv_list[sel3].price * cant
        return increase_wallet


def corps_menu(wallet, crops, individual, seed, fert, medic):

    print('Opciones:\n  ' +
          '1 - Ver mi inventario de cultivos\n  ' +
          '2 - Vender un producto de cultivos\n  ' +
          '3 - Comprar productos de cultivo\n  ' +
          '4 - Comprar mejoras para mis cultivos')
    sel2 = input('Ingrese lo que desea hacer: ')
    if sel2 == '1':
        print('INVENTARIO')
        show_crop_products_buyable(fert, medic)
        show_crop_products_sellable(individual, seed)
    elif sel2 == '2':
        print('Menú de ventas:\n  ' +
              '1 - Productos plantables\n  ' +
              '2 - Productos consumibles')
        select = input('Ingresa la opción a vender: ')
        if select == '1':
            return sell(seed, 'Productos plantables')
        elif select == '2':
            return sell(individual, 'Productos consumibles')

    elif sel2 == '3':
        print('Menú de compras:\n  ' +
              '1 - Productos plantables\n  ' +
              '2 - Productos medicinales\n  ' +
              '3 - Fertilizantes')
        select = input('Ingresa qué quieres comprar: ')
        if select == '1':
            return buy(buy_seed, 'Productos plantables', wallet, seed)

        if select == '2':
            return buy(buy_medic, 'Productos medicinales', wallet, medic)

        if select == '2':
            return buy(buy_fert, 'Fertilizantes', wallet, fert)

    elif sel2 == '3':
        print('MEJORAS:\n  ' +
              'Precio: 500 tornillos (Aumenta el nivel de productividad de tus plantas +1)')
        if wallet - 500 <= 0:
            print('No tienes suficientes tornillos para comprar una mejora')
        else:
            remove_wallet = -500
            for crop in crops:
                crop.productivity += 1
            return remove_wallet


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
                    coins_add = amount_sell_item * sell_item['Precio']
                    sell_item['Cantidad'] = sell_item['Cantidad'] - amount_sell_item
            else:
                print('No puedes vender esa cantidad de objetos.')
                return sell_item_farm(inventory_animals, wallet, animals)
        else:
            print('Vaya ese item, no lo encontré.')
            return sell_item_farm(inventory_animals, wallet, animals)
        return coins_add

    elif sel_farm == '2':
        coins_remove = 0
        print('Estos son los precios:\n' + '1x Mejora de productividad = 600 tornillos\n')
        op = input('¿Deseas adquirirla? (s/n)')
        if op == 's':
            if wallet - 600 >= 0:
                coins_remove = -600
                for animal in animals:
                    animal.productivity += 1
            else:
                print('Parece, que no puedes completar esta compra de productividad.')
        elif op == 'n':
            pass

        return coins_remove


def main_trading(inventory_animals: list[dict], wallet: int, animals, crops: list[Crop], seed: list[CropProduct],
                 fert: list[Fertilizer], medic: list[Medicine], individual: list[CropProduct]):
    print('COMPRA Y VENTA')
    print('Bienvenido a la sección de compra y venta de productos.')
    print('OPCIONES:\n  ' +
          '1 - Productos de cultivo\n  ' +
          '2 - Productos de la granja de animales\n  ')
    sel = input('Ingrese la sección a la que deseas ingresar: ')
    if sel == '1':
        wallet += corps_menu(wallet, crops, individual, seed, fert, medic)
        return {'Wallet': wallet,
                'Plantables': seed,
                'Individuales': individual,
                'Fertilizantes': fert, 'Medicamentos': medic, 'type': 'crop'}
    elif sel == '2':
        wallet += sell_item_farm(inventory_animals, wallet, animals)
        return {'Wallet': wallet, 'Inventario': inventory_animals, 'type': 'animal'}
