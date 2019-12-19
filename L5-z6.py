'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество.
 Важно, чтобы для каждого предмета не обязательно были все типы занятий.
 Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''


def read_from_file():
    joint, res_list, res_dict, sum_list = 0, [], {}, 0
    try:
        with open('z6.dat', 'r', encoding='utf-8') as f:
            for line in f:
                line_list = line.split()
                #print(line_list)
                for elem in line_list:
                    res_list.append("".join(filter(lambda b: b.isnumeric(), elem)))
                    sum_list = sum([int(x) for x in res_list if x.isdigit()])
                #print(res_list)
                res_list[:] = []
                res_dict[line_list[0]] = sum_list
                del sum_list
            print(res_dict)
    except IOError:
        print("Ошибка ввода-вывода!")



while True:
    read_from_file()
    answer = (input('Press any kay to exit'))
    break
