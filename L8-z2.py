'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class OwnError(Exception):
    def __init__(self, msg):
        self.msg = msg


dividend = input('Введите делимое: ')
divider = input('Введите делитель: ')

try:
    if (dividend.isalpha()) or (divider.isalpha()):
        raise OwnError("Только числа!")

    int_dividend = int(dividend)
    int_divider = int(divider)

    if int_divider == 0:
        raise OwnError("Деление на 0!")

except OwnError as Err:
    print(Err)
else:
    print(int_dividend / int_divider)
