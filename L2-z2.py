'''
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо
 использовать функцию input().

'''
#Вариант 1
#my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'end']
my_list = input('Введите элементы списка: ').split()
len_list = len(my_list) - 1
for i in range(0, len_list, 2):
    if my_list[i + 1] != ' ':
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    else:
        my_list.append(my_list[i])
print(my_list)

'''
#Вариант 2
# my_list, my_list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'end'], []
my_list, my_list1 = input('Введите элементы списка: ').split(), []
my_list.append(' ')
len_list = len(my_list) - 1
for i in range(0, len_list, 2):
    if my_list[i + 1] != ' ':
        my_list1.append(my_list[i + 1])
        my_list1.append(my_list[i])
    else:
        my_list1.append(my_list[i])
print(my_list1)
'''

