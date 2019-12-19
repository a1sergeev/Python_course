'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
from L5.serializator import serialize

def Calculations():
    joint, count, average_profit, res_list, res_dict = 0, 0, 0, [], {}
    try:
        with open('z7.dbt', 'r', encoding='utf-8') as f:
            for line in f:
                line_list = line.split()
                profit = int(line_list[-2]) - int(line_list[-1])
                if profit > 0:
                    joint += profit
                    count += 1
                res_dict = {line_list[0] : profit}
                res_list.append(res_dict)
            average_profit = joint / count
            res_list.append({"average_profit": average_profit})
            print(res_list)
            serialize(res_list)

    except IOError:
        print("Ошибка ввода-вывода!")
    except ValueError:
        print("Только числа!")


answer = None
while answer != 'exit':
    Calculations()
    answer = (input('Enter - продолжить, exit - выход: ')).lower()
    print('Successfully! ')
    break

