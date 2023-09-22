from animals.cow import Cow
from animals.chicken import Chicken
from animals.sheep import Sheep
from animals.goat import Goat
from animals.bee import Bee


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
    animals: list[Cow | Chicken | Sheep | Bee | Goat] = []
    print('Bienvenido a: "Cuidado de Animales"')
    op = ''
    while op != '7':
        print('\nElige que hacer:\n1. Adquirir un animal 2. Alimentar'
              ' 3. Acariciar 4. Limpiar 5. Recolectar Recursos 6. Curar 7. Salir')
        op = input()
        if op == '1':
            animal = choose_animal()
            animals.append(animal)
            print(f'Felicidades {animal.name} se ha unido a tu granja! ¡Espero la cuides lo mejor posible!')
            continue
        if op == '2':
            pass

    return animals
