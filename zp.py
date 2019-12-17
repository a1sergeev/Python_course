'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

try:
    hours = int(argv[1])
    rate = int(argv[2])
    percent = int(argv[3])

    bonus = (hours * rate) * percent/100
    salary = hours * rate + bonus
    print(f'{salary:.2f} rub')
except ValueError:
    print(f'Только числа! ')

