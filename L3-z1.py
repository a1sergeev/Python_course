'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

'''

def div_fun(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Деление на 0!")
        quit()

ans = ' '
while ans != 'exit':
    try:
        print(f'{div_fun(float(input("a = ")), float( input("b = "))):.2f}')
        ans = input('Enter - продолжить, exit - выход: ')
    except ValueError:
        print("Только числа!")


