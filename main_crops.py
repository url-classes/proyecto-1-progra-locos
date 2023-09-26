from cultivation.crops.wheat import Wheat
from cultivation.crops.corn import Corn
from cultivation.crops.cotton import Cotton
from cultivation.crops.potato import Potato
from cultivation.crops.rice import Rice
from cultivation.crops.crop_product import CropProduct

from cultivation.plagues.aphid import Aphid
from cultivation.plagues.caterpillar import Caterpillar
from cultivation.plagues.tripp import Tripp

import time

ground: list[Corn | Cotton | Potato | Rice | Wheat] = []
plagues: list[Aphid | Caterpillar | Tripp] = []
seed_products: list[CropProduct] = [
    CropProduct('Semilla de maíz', 10, 12.0, False),
    CropProduct('Semilla de trigo', 10, 20, False),
    CropProduct('Papas de plantación', 10, 36, False),
    CropProduct('Semilla de arroz', 10, 10, False),
    CropProduct('Semilla de algodón', 10, 20.0, False)
]
ind_products: list[CropProduct] = [
    CropProduct('Mazorcas', 0, 20.0, True),
    CropProduct('Harina', 0, 17.0, True),
    CropProduct('Papas', 0, 36.0, True),
    CropProduct('Arroz', 0, 8.0, True),   
    CropProduct('Algodón', 0, 45.0, True)
]

seed_plant = {
    '-Planta de maíz-': 0,
    '-Planta de trigo-': 1,
    '-Planta de papas-': 2,
    '-Planta de arroz-': 3,
    '-Planta de algodón-': 4
}


def input_timer(prompt):
    start = time.time()
    character = input(prompt)
    end = time.time()
    total_time = end - start
    for crop in ground:
        crop.growth(total_time)
        crop.get_sick(total_time)
        crop.actual_plague.set_performance(total_time)
        death()

    return character


def death():
    for plant in ground:
        if plant.health_lvl == 0:
            ground.remove(plant)
            print(f'¡¡¡Una {plant.plant_name} ha muerto!!!')


def add_crop():
    spent = 0
    for i in seed_products:
        if i.amount == 0:
            spent += 1
    if spent == 5:
        print('¡Lo siento!, pero no te quedan más semillas')
    else:
        print('ELIGE UNA SEMILLA PARA PLANTAR:\n ' +
              '1 - Semilla de maiz\n ' +
              '2 - Semilla de trigo\n ' +
              '3 - Papas de plantación\n ' +
              '4 - Semilla de arroz\n ' +
              '5 - Semilla de algodón')
        sel = int(input_timer(': '))
        seed_products[sel - 1].amount -= 1
        if sel == 1:
            ground.append(Corn())
            print('¡Haz agregado una planta de maiz!')
        elif sel == 2:
            ground.append(Wheat())
            print('¡Haz agregado una planta de trigo!')
        elif sel == 3:
            ground.append(Potato())
            print('¡Haz agregado una planta de papas!')
        elif sel == 4:
            ground.append(Rice())
            print('¡Haz agregado una planta de arroz!')
        elif sel == 5:
            ground.append(Cotton())
            print('¡Haz agregado una planta de algodón!')


def rinse():
    for crop in ground:
        crop.water_plant()
    print('Haz regado todos tus cultivos. ¡+15 puntos de salud!')


def collect():
    print('RECOLECTAR PRODUCTOS')
    not_ready = 0
    for crop in ground:
        if crop.growth_phase == 'Madura':
            print(str(ground.index(crop) + 1) + f'-{crop.plant_name}')
            print(str(crop) + '\n----------------------------------------------------------------')
        else:
            not_ready += 1
    if not_ready == len(ground):
        print('¡Lo siento!, pero no te quedan más semillas')
    else:
        sel = int(input_timer('Selecciona una de las plantas para cosechar: '))
        k = seed_plant[ground[sel - 1].plant_name]
        seed_products[k].amount += 1
        ind_products[k].amount += 1
        print(f'¡Felicidades! has obtenido +1 {seed_products[k].name} ' +
              f'y +1 {seed_products[k].name}')


def fertilize():
    for crop in ground:
        crop.health_lvl += 10


def medic():
    pass


def crop_stats():
    for crop in ground:
        print(str(ground.index(crop) + 1) + f' -{crop.plant_name}')
        print(str(crop) + '\n----------------------------------------------------------------')



def crop_product_stats():
    print('TU INVENTARIO')
    print('Productos consumibles:')
    spent = 0
    for product in ind_products:
        if product.amount == 0:
            spent += 1
        else:
            print(product)
    if spent == 5:
        print('--No tienes productos consumibles--')
    print('Productos plantables:')
    spent = 0
    for product in seed_products:
        if product.amount == 0:
            spent += 1
        else:
            print(product)
    if spent == 5:
        print('--No tienes productos plantables--')


def main():
    print('---Sistema de Cultivos---')
    while True:
        print('¿QUE QUIERES HACER?:\n 1 - Agregar un cultivo\n ' +
              '2 - Ver el estado de tus cultivos\n ' +
              '3 - Regar mis cultivos\n ' +
              '4 - Recolectar cosechas\n ' +
              '5 - Fertilizar la tierra\n ' +
              '6 - Medicar un cultivo\n ' +
              '7 - Revisar mis productos de cultivo')

        sel = input_timer(': ')
        if sel == '1':
            add_crop()
        elif sel == '2':
            print('ESTADO DE TUS CULTIVOS')
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
        option2 = input_timer('¿Regresar al menú? S/N: ')
        if option2 == 'S':
            continue
        else:
            break

main()
