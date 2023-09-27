from main_animals import main_animals
animals_farm: list = []

animals_main = main_animals(animals_farm)
for animal in animals_main[0]:
    animals_farm.append(animal)

