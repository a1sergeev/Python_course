'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv
hours = argv[1]
rate = argv[2]
percent = argv[3]

def pay(hours, rate, percent):
    try:
        #hours = int(input('Выработка в часах: '))
        #rate = int(input('Cтавка работника в час: '))
        bonus = (hours * rate) * percent/100
        salary = hours * rate + bonus
        return f'{salary:.2f} rub'
    except ValueError:
        return f'Только числа! '

#if __name__ == '__main__':
    #print(pay())
