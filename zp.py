'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

def pay():
    try:
        hours = int(input('Выработка в часах: '))
        rate = int(input('Cтавка работника в час: '))
        bonus = (hours * rate) * int(input('Сколько процентов премии: '))/100
        salary = hours * rate + bonus
        return f'{salary:.2f} rub'
    except ValueError:
        return f'Только числа! '

if __name__ == '__main__':
    print(pay())