'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import count, cycle

def func1():
    start = int(input('start= '))
    stop = int(input('stop= '))
    step = int(input('step= '))
    [quit() if el > stop else print(el, end=' ') for el in count(start, step)]


def func2():
    stop = int(input('stop= '))
    rand, c = ['apple', 'яблоко', 'orange', 'апельсин', 'kiwi', 'киви', 'watermelon', 'арбуз'], 1
    for elem in cycle(rand):
        if c > stop:
            break
        print(elem, end=' ')
        c+=1




if __name__ == '__main__':
    #func1()

    func2()