from input_timer import input_timer


def add_activity(dates: list):
    dates.append(
        {
         'Actividad': input('Ingresa el nombre de la actividad: '),
         'Tiempo': float(input('Ingresa en cuantos minutos quieres que se active el recordatorio: ')),
         'own_time': 0
         }
    )


def post_activity(dates: list):
    show_activities(dates)
    sel = int(input_timer('Ingresa el número de la actividad a posponer: ', dates)) - 1
    minutes = int(input_timer('Ingresa la cantidad de minutos para posponer tu actividad: ', dates))
    dates[sel]['Tiempo'] = 0
    dates[sel]['Tiempo'] += minutes


def show_activities(dates: list):
    print('AGENDA ACTUAL:')
    for date in dates:
        print(f'Actividad No.{dates.index(date) + 1}: ')
        print(f'  - Nombre: {date["Actividad"]}\n  - Tiempo restante: {date["Tiempo"]}')


def delete_activity(dates: list):
    show_activities(dates)
    sel = int(input_timer('Ingresa el número de la actividad a eliminar: ', dates)) - 1
    dates.remove(dates[sel])


def main_calendar(dates: list):
    while True:
        print('CALENDARIO:\n' +
              '1 - Agendar una nueva actividad\n' +
              '2 - Posponer una actividad\n' +
              '3 - Eliminar\n' +
              '4 - Ver mis actividades agendadas\n' +
              '5 - Salir')
        sel = input_timer('¿Qué deseas hacer?: ', dates)

        if sel == '1':
            add_activity(dates)
        elif sel == '2':
            post_activity(dates)
        elif sel == '3':
            delete_activity(dates)
        elif sel == '4':
            show_activities(dates)
        elif sel == '5':
            return dates
