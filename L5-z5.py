'''
 Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''


def write_to_file():
    try:
        with open('z5.txt', 'w', encoding='utf-8') as f:
            text = input('Введите числа через пробел: ').split()
            for num in text:
                f.write(num + ' ')
        print(f'Записано в {f.name}')
    except IOError:
        print("Ошибка ввода-вывода!")


def read_from_file():
    try:
        with open('z5.txt', 'r', encoding='utf-8') as f:
            for num in f:
                num_list = num.split()
                print('Сумма = ', sum([int(x) for x in num_list]))
    except IOError:
        print("Ошибка ввода-вывода!")
    except ValueError:
        print("Только числа!")


answer = None
while answer != 'exit':
    write_to_file()
    read_from_file()
    answer = (input('Enter - продолжить, exit - выход: ')).lower()
