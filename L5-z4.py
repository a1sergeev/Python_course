'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
'''
import os
from L5.dict_num import dict_RU

os.remove("z4_output.txt")

f_in = open("z4_input.txt", "r", encoding='utf-8')
for line in f_in:
    str_split = line.split()
    num = int(str_split[-1])
    with open('z4_output.txt', 'a', encoding='utf-8') as f_out:
        f_out.writelines('{} — {} {}'.format(dict_RU[num], str_split[-1], "\n"))
    # f_out.write(dict_RU[num])
    # f_out.writelines(str_split[1:])
    # f_out.writelines("\n")
print(f'Записано в файл {f_out.name}')
f_in.close()
