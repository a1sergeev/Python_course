'''
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
'''

a = 10
b = a ** 2
print('Ответ =', a + b)  # 110
print('-'*12)

a = float(input('Введите a: '))
b = float(input('Введите b: '))
x = str(input('Введите операцию, (+, -, *, **, /, div, mod): '))
if (x == "/" or x == "mod" or x == "div") and b == 0:
    print("Деление на 0!")
elif x == "+":
    print(f'{a} {x} {b} = ', a + b)
elif x == "-":
    print(f'{a} {x} {b} = ', a - b)
elif x == "*":
    print(f'{a} {x} {b} = ', a * b)
elif x == "**":
    print(f'{a} {x} {b} = ', a ** b)
elif x == "/":
    print(f'{a} {x} {b} = ', f'{(a / b):.2f}')
elif x == "div":
    print(f'{a} {x} {b} = ', a // b)
elif x == "mod":
    print(f'{a} {x} {b} = ', a % b)
elif x == "help" or "?":
    print('+ -сложение a и b')
    print('- -из a вычитаем b')
    print('* -умнажаем a на b')
    print('** -возводим a в степень b')
    print('/ -a делим на b')
    print('div - получить целую часть от деления a на b')
    print('mod -остаток от деления a на b')
else:
    print('Не понимаю. Возможные операции \n (+, -, *, **, /, div, mod, help или ?)')
