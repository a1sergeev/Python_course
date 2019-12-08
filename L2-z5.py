'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

'''
# Вариант1
my_list = [10, 7, 5, 3, 3, 2]
len_list = len(my_list)
ans = ' '
try:
    n = int(input('Введите значение: '))
    my_list.reverse()
    for i in range(len_list):
        if n <= my_list[i] and n < my_list[-1]:
            my_list.insert(my_list.index(my_list[i]), n)
            break
        elif n > my_list[-1]:
            my_list.insert(my_list[-1], n)
            break
    my_list.reverse()
    print(*my_list, sep=', ')
except ValueError:
    print('Только числа ')

'''
# Вариант 2
my_list = [7, 5, 3, 3, 2]
try:
    n = input('Введите значение или exit- для выхода: ')
    while True:
        if (n != 'exit') and (int(n) > 0):
            my_list.append(int(n))
            my_list.sort(reverse=True)
            n = input('Введите значение или exit- для выхода: ')
            continue
        elif n == 'exit':
            break
        else:
            print('Только положительный числа')
            continue
    print(*my_list, sep=', ')
except ValueError:
    print('Только положительный числа')

'''
