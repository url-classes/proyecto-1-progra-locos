import time


def add_activity(dates: list):
    dates.append(
        {
         'Actividad': input('Ingresa el nombre de la actividad: '),
         'Tiempo': int(input('Ingresa en cuantos minutos quieres que se active el recordatorio: '))
         }
    )


def input_timer(prompt: str, dates: list):
    start = time.time()
    output = input(prompt)
    end = time.time()
    final = end - start
    minutes = final // 60
    for date in dates:
        date['Tiempo'] -= minutes
        if date['Tiempo'] <= 0:
            print(f'La actividad {date["Actividad"]} ¡Se ha vencido!.')

    return output


def main_calendar(dates: list):
    while True:
        print('CALENDARIO:\n' +
              '1 - Agendar una nueva actividad\n' +
              '2 - Posponer una actividad\n' +
              '3 - Eliminar\n' +
              '4 - Ver mis actividades agendadas\n' +
              '5 - Salir')
        sel = input_timer('¿Qué deseas hacer?: ')

        if sel == '1':
            add_activity(dates)
        elif sel == '2':
            pass
        elif sel == '3':
            pass
        elif sel == '4':
            pass
        elif sel == '5':
            return dates
