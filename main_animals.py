from animals import Cow
from animals import Chicken
from animals import Sheep
from animals import Goat
from animals import Bee
from animals import Animal
import threading

foods = [{'id': 1, 'Name': 'Heno', 'Hunger': 5},
         {'id': 2, 'Name': 'Paja', 'Hunger': 9},
         {'id': 3, 'Name': 'Granos', 'Hunger': 12},
         {'id': 4, 'Name': 'Legumbres', 'Hunger': 15},
         {'id': 5, 'Name': 'Granos Premium', 'Hunger': 22}]


def conts(consume_hunger, consume_hapiness, consume_cleaness, is_live):
    thread_hunger = threading.Thread(target=consume_hunger)
    thread_hunger.start()

    thread_hapiness = threading.Thread(target=consume_hapiness)
    thread_hapiness.start()

    thread_cleaness = threading.Thread(target=consume_cleaness)
    thread_cleaness.start()

    thread_life = threading.Thread(target=is_live)
    thread_life.start()


def stroke_animal(animals: list):
    found_animal = False

    print('Acariciar a tu animal, aumentará el nivel de felicidad dependiendo de cuánto tiempo quieres esperar.')
    print('Ingresa el nombre del animal que deseas acariciar: ')
    for animal in animals:
        print(animal.name)
    animal_stroke = input()
    for animal in animals:
        if animal.name == animal_stroke:
            animal_stroke = animal
            found_animal = True
    time_ = int(input('Ingresa el tiempo que quieres que descanse tu animalito, '
                      'recuerda que tu también debes hacerlo. '))
    if found_animal:
        animal_stroke.stroke(time_)
        print(f'Wow, {animal_stroke.name} subió {2*time_}pts de felicidad')
    else:
        print('Wow, el animal no fue encontrado.')
        stroke_animal(animals)


def clean_animal(animals: list):
    found_animal = False

    print('Limpiar a tu animal, aumentará el nivel de limpieza, '
          'evitando así enfermedades, dependiendo de cuánto tiempo quieres esperar.')
    print('Ingresa el nombre del animal que deseas darle un buen baño: ')
    for animal in animals:
        print(animal.name)
    animal_clean = input()
    for animal in animals:
        if animal.name == animal_clean:
            animal_clean = animal
            found_animal = True
    print('Ingresa el tiempo que quieres que limpiar tu animalito, recuerda que tu también debes esperar. ')
    time_ = int(input('Por cada 13 subirá un punto de limpieza.'))
    if found_animal:
        animal_clean.clean(time_)
        print(f'Wow, {animal_clean.name} subió {time_//13}pts de limpieza')
    else:
        print('Wow, el animal no fue encontrado.')
        stroke_animal(animals)


def eat_animal(animals: list):
    found_animal = False
    found_food = False

    print('Tenemos 5 opciones para alimentar a tus animales')
    print('1. Heno 2. Paja 3. Granos 4. Legumbres 5. Granos Premium')
    print('Ingresa el número correspondiente a la comida que requieres: ')
    id_food = int(input(''))
    for food in foods:
        if id_food == food['id']:
            id_food = food['Hunger']
            found_food = True
            break

    print('Ingresa el nombre del animal que deseas alimentar: ')
    for animal in animals:
        print(animal.name)
    animal_look = input()
    for animal in animals:
        if animal.name == animal_look:
            animal_look = animal
            found_animal = True

    if found_animal and found_food:
        animal_look.eat(id_food)
    else:
        print('Wow, el animal no fue encontrado y/o la comida no existe.')
        eat_animal(animals)


def recolect_product_animal(animals: list):
    found_animal = False

    print('Ingresa el nombre del animal que deseas alimentar: ')
    for animal in animals:
        print(animal.name)
    animal_look = input()
    for animal in animals:
        if animal.name == animal_look:
            animal_look = animal
            found_animal = True

    if found_animal and found_food:
        animal_look.eat(id_food)
    else:
        print('Wow, el animal no fue encontrado y/o la comida no existe.')
        eat_animal(animals)


def choose_animal():

    print('Elige a que animal criar:\n1. Vaca 2. Gallina '
          '3. Oveja 4. Abeja 5. Cabra')

    animal_chosen = input()

    if animal_chosen == '1':
        print('Has elegido a la vaca, escoge su nombre: ')
        return Cow(input('Nombre del animal: '))
    elif animal_chosen == '2':
        print('Has elegido a la gallina, escoge su nombre: ')
        return Chicken(input('Nombre del animal: '))
    elif animal_chosen == '3':
        print('Has elegido a la oveja, escoge su nombre: ')
        return Sheep(input('Nombre del animal: '))
    elif animal_chosen == '4':
        print('Has elegido a la abeja, escoge su nombre: ')
        return Bee(input('Nombre del animal: '))
    elif animal_chosen == '5':
        print('Has elegido a la cabra, escoge su nombre: ')
        return Goat(input('Nombre del animal: '))
    else:
        print('Wow, ese animal no me lo sé, vuelve a intentar.')
        return choose_animal()


def main_animals() -> list:
    inventory = []
    animals: list[Cow | Chicken | Sheep | Bee | Goat] = []
    print('Bienvenido a: "Cuidado de Animales"')
    op = ''
    while op != '7':
        print('\nElige que hacer:\n1. Adquirir un animal 2. Alimentar'
              ' 3. Acariciar 4. Limpiar 5. Recolectar Recursos 6. Curar 7. Ver estado 8. Salir')
        op = input()
        if op == '1':
            animal = choose_animal()
            conts(animal.consume_hunger, animal.consume_happiness, animal.consume_cleaness, animal.is_live)
            animals.append(animal)
            print(animal.production)
            print(f'Felicidades {animal.name} se ha unido a tu granja! ¡Espero la cuides lo mejor posible!')
            continue
        if op == '2':
            eat_animal(animals)
        if op == '3':
            stroke_animal(animals)
        if op == '4':
            clean_animal(animals)
        if op == '5':
            recolect_product_animal(animals)
    return [animals, inventory]


