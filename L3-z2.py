'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def anketa(name, surname, birth, city, email, tel):
    try:
        if 1919 < int(birth) < 2019 and name.isalpha() and surname.isalpha() and city.isalpha() and tel.isdigit():
            age = 2019 - int(birth)
            print(
                f'Данные:  {name.title()} {surname.title()}, {age} лет, {birth} года рождения, проживающий '
                f'в г. {city.title()}, тел: {tel[0]}({tel[1:4]})-{tel[4:7]}-{tel[7:9]}-{tel[9:11]}, e-mail: {email}')
        else:
            print('Введены не корректные данные')
    except ValueError:
        print('Год рождения введён не правильно!')


name1, lastname, birth1, city1, email1, tel1 = input('Имя: '), input('Фамилия: '), input('Год рождения: '), input(
    'Город проживания: '), input('E-mail: '), input('Введите номер телефона, в формате 89001234567: ')
anketa(surname=lastname, name=name1, city=city1, birth=birth1, tel=tel1, email=email1)
