import time


def input_timer(prompt: str, dates: list):
    start = time.time()
    output = input(prompt)
    end = time.time()
    final = end - start

    for date in dates:
        date['own_time'] += final
        minutes = date['own_time'] / 60
        date['Tiempo'] -= minutes
        date['Tiempo'] = round(date['Tiempo'], 1)
        if date['Tiempo'] <= 0:
            print(f'La actividad {date["Actividad"]} ¡Se ha vencido!.')

    return output
