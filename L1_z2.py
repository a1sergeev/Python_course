'''
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк.
'''
#17999  04:59:59
# 9612 02:40:12
hO, mO,sO = '', '', ''
input_sec = int(input('Введите время в секундах: '))
hh = input_sec // 3600
if hh < 10:
    hO = 0
# mm = ((inpit_sec/3600)-hh)*60
mm = (input_sec % 3600) // 60
if mm < 10:
    mO = 0
ss = (((input_sec % 3600) / 60) - mm) * 60
if ss < 10:
    sO = 0
print(f'{hO}{hh}:{mO}{mm}:{sO}{ss:.0f}')