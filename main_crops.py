from cultivation.crops.wheat import Wheat
from cultivation.crops.corn import Corn
from cultivation.crops.cotton import Cotton
from cultivation.crops.potato import Potato
from cultivation.crops.rice import Rice
from cultivation.crops.crop_product import CropProduct

from cultivation.plagues.aphid import Aphid
from cultivation.plagues.caterpillar import Caterpillar
from cultivation.plagues.tripp import Tripp

from cultivation.medication.fertilizer import Fertilizer
from cultivation.medication.medicine import Medicine

import time

plagues: list[Aphid | Caterpillar | Tripp] = []
seed_products: list[CropProduct] = [
    CropProduct('Semilla de maíz', 3, 12.0, False),
    CropProduct('Semilla de trigo', 3, 20, False),
    CropProduct('Papas de plantación', 3, 36, False),
    CropProduct('Semilla de arroz', 3, 10, False),
    CropProduct('Semilla de algodón', 3, 20.0, False)
]
ind_products: list[CropProduct] = [
    CropProduct('Mazorcas', 0, 20.0, True),
    CropProduct('Harina', 0, 17.0, True),
    CropProduct('Papas', 0, 36.0, True),
    CropProduct('Arroz', 0, 8.0, True),   
    CropProduct('Algodón', 0, 45.0, True)
]
medic_products: list[Medicine] = [
    Medicine('Medicamento Nivel 1', 45.0, 4, 50, 10),
    Medicine('Medicamento Nivel 2', 90.0, 2, 100, 15)
]

fertilizers: list[Fertilizer] = [
    Fertilizer('Fertilizante Nivel 1', 20.0, 4, 180, 10),
    Fertilizer('Fertilizante Nivel 2', 40.0, 2, 1000, 15)
]

seed_plant = {
    '-Planta de maíz-': 0,
    '-Planta de trigo-': 1,
    '-Planta de papas-': 2,
    '-Planta de arroz-': 3,
    '-Planta de algodón-': 4
}


def input_timer(prompt, ground):
    start = time.time()
    character = input(prompt)
    end = time.time()
    total_time = end - start
    for crop in ground:
        crop.growth()
        crop.get_sick(total_time)
        crop.set_lifespan(total_time)
        crop.plague_attack(total_time)

        death(ground)

    return character


def death(ground):
    for plant in ground:
        if plant.health_lvl == 0:
            ground.remove(plant)
            print(f'¡¡¡Una {plant.plant_name} ha muerto!!!')


def add_crop(ground):
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
        sel = int(input_timer(': ', ground))
        seed_products[sel - 1].amount -= 1
        if sel == 1:
            ground.append(Corn())
            print('¡Haz agregado una planta de maiz!')
        elif sel == 2:
            ground.append(Wheat())
            print('¡Has agregado una planta de trigo!')
        elif sel == 3:
            ground.append(Potato())
            print('¡Haz agregado una planta de papas!')
        elif sel == 4:
            ground.append(Rice())
            print('¡Haz agregado una planta de arroz!')
        elif sel == 5:
            ground.append(Cotton())
            print('¡Haz agregado una planta de algodón!')


def rinse(ground):
    for crop in ground:
        crop.water_plant()
    print('Haz regado todos tus cultivos. ¡+15 puntos de salud!')


def collect(ground):
    print('RECOLECTAR PRODUCTOS')
    not_ready = 0
    for crop in ground:
        if crop.growth_phase == 'Madura':
            print(str(ground.index(crop) + 1) + f'-{crop.plant_name}')
            print(str(crop) + '\n----------------------------------------------------------------')
        else:
            not_ready += 1
    if not_ready == len(ground):
        print('¡Lo siento!, pero ninguna de tus plantas está lista para cosecharse')
    else:
        sel = int(input_timer('Selecciona una de las plantas para cosechar: ', ground))
        k = seed_plant[ground[sel - 1].plant_name]
        adder = 2 * ground[sel - 1].productivity
        seed_products[k].amount += adder
        ind_products[k].amount += adder
        ground.remove(ground[sel - 1])

        print(f'¡Felicidades! has obtenido +{adder} {seed_products[k].name} ' +
              f'y +{adder} {ind_products[k].name}')
        print('La planta cosechada se ha removido del suelo.')


def fertilize(ground):
    print('FERTILIZAR:')
    for crop in ground:
        print(str(ground.index(crop) + 1) + f'-{crop.plant_name}')
        print(str(crop) + '\n----------------------------------------------------------------')
    sel = int(input('Selecciona la planta a fertilizar: ')) - 1
    i = 0
    for product in fertilizers:
        if product.amount != 0:
            i += 1
            print(str(i) + '. ' + str(product))

    if i != 0:
        sel2 = int(input('Selecciona el fertilizante a utilizar: ')) - 1
        if len(ground) == 0:
            print('No tienes plantas en tu terreno.')
        else:
            ground[sel].fertilize(fertilizers[sel2])

        fertilizers[sel2].amount -= 1

        print(f'!La -{ground[sel].plant_name}- ha sido fertilizada!')
    else:
        print('¡Ya no tienes más fertilizante!')


def medic(ground):
    print('MEDICAR:')
    not_ill_num = 0
    for crop in ground:
        if crop.actual_plague.name == 'Ninguna':
            not_ill_num += 1
        else:
            print(str(ground.index(crop) + 1) + f'-{crop.plant_name}')
            print(str(crop) + '\n----------------------------------------------------------------')
    if not_ill_num == len(ground):
        print('Ninguna de tus plantaciones necesita medicación.')
    else:
        sel = int(input_timer('Selecciona la planta a medicar: ', ground)) - 1
        i = 0
        for product in medic_products:
            if product.amount != 0:
                i += 1
                print(str(i) + '. ' + str(product))
        if i != 0:
            sel2 = int(input_timer('Selecciona el medicamento a utilizar: ', ground)) - 1
            if len(ground) == 0:
                print('No tienes plantas en tu terreno.')
            else:
                ground[sel].medic(medic_products[sel2])

            prompt = ''
            if medic_products[sel2].plague_activity_change == 100:
                prompt = 'plaga eliminada.'
            else:
                prompt = '-50 de rendimiento de la plaga.'

            print(f'!La -{ground[sel].plant_name}- ha sido medicada! ' +
                  f'+{medic_products[sel2].plant_health_increment} de salúd y {prompt}')
        else:
            print('¡Ya no tienes medicamentos!')


def crop_stats(ground):
    for crop in ground:
        print(str(ground.index(crop) + 1) + f' -{crop.plant_name}')
        print(str(crop) + '\n----------------------------------------------------------------')


def general_show_function(lisst, name_list):
    print(f'{name_list}:')
    spent = 0
    for product in lisst:
        if product.amount == 0:
            spent += 1
        else:
            print(str(lisst.index(product) + 1) + '. ' + str(product))
    if spent == len(ind_products):
        print(f'--No tienes {name_list}--')


def crop_product_stats():
    print('TU INVENTARIO')
    general_show_function(ind_products, 'Productos consumibles')
    general_show_function(seed_products, 'Productos plantables')
    general_show_function(fertilizers, 'Fertilizantes')
    general_show_function(medic_products, 'Medicamentos')


def main_crops(ground: list[Corn | Cotton | Potato | Rice | Wheat]):
    print('---Sistema de Cultivos---')
    while True:
        print('¿QUE QUIERES HACER?:\n 1 - Agregar un cultivo\n ' +
              '2 - Ver el estado de tus cultivos\n ' +
              '3 - Regar mis cultivos (+15 de salúd cada uno y -30 segundos de cambio de fase)\n ' +
              '4 - Recolectar cosechas\n ' +
              '5 - Fertilizar la tierra\n ' +
              '6 - Medicar un cultivo\n ' +
              '7 - Revisar mis productos de cultivo\n ' +
              '8 - Salir')

        sel = input_timer(': ', ground)
        if sel == '1':
            add_crop(ground)
        elif sel == '2':
            print('ESTADO DE TUS CULTIVOS')
            crop_stats(ground)
        elif sel == '3':
            rinse(ground)
        elif sel == '4':
            collect(ground)
        elif sel == '5':
            fertilize(ground)
        elif sel == '6':
            medic(ground)
        elif sel == '7':
            crop_product_stats()
        elif sel == '8':
            return {'Cultivos': ground,
                    'Productos individuales': ind_products,
                    'Productos plantables': seed_products,
                    'Productos medicinales': medic_products,
                    'Fertilizantes': fertilizers}

