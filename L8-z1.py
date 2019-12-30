'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

'''
from L8.dict_num import dict_dd, dict_mm, dict_yyyy


class Date:
    def __init__(self, date):
        self.date = date
        Date.digital_date(self.date)

    @classmethod
    def digital_date(cls, str_date):
        for i in range(len(str_date)):
            str_list = str_date.lower().split('-')
        dd = [key for key, value in dict_dd.items() if str_list[0] == value]
        mm = [key for key, value in dict_mm.items() if str_list[1] == value]
        yy = [key for key, value in dict_yyyy.items() if str_list[2] == value]
        if yy == []:
            yy = [0]
        print(dd, mm, yy)
        input('press any key')
        Date.verification(dd, mm, yy)

    @staticmethod
    def verification(dd, mm, yy):
        if (yy[0] == 0):
            print("{}.{}.{} года".format(dd[0], mm[0], *yy))  # Пока не реализованно
        if 0 < dd[0] <= 31 and 0 < mm[0] <= 12 and 0 < yy[0]:
            if dd[0] <= 31 and mm[0] in (1, 3, 5, 7, 8, 10, 12):
                print("{}.{}.{} года".format(dd[0], mm[0], yy[0]))
            elif dd[0] <= 30 and mm[0] in (4, 6, 9, 11):
                print("{}.{}.{} года".format(dd[0], mm[0], yy[0]))
            elif mm[0] == 2 and dd[0] <= 29:
                if (yy[0] % 4 == 0) and (yy[0] % 100 != 0) or (yy[0] % 400 == 0):
                    print("{}.{}.{} года".format(dd[0], mm[0], yy[0]))
                elif dd[0] <= 28:
                    print("{}.{}.{} года".format(dd[0], mm[0], yy[0]))
                else:
                    print("В феврале {} года {} только 28 дней {}".format(yy[0], '\x1b[1;31m', '\x1b[0m'))
            else:
                print("{}-м месяце {} меньше дней {} ".format(mm, '\x1b[1;31m', '\x1b[0m'))
        else:
            print("{} Введена не корректная дата {}".format('\x1b[1;31m', '\x1b[0m'))


date_1 = input('Введите дату \n(В формате: тридцать первое-декабря-дветысячи девятнадцатого): ')
d = Date(date_1)
