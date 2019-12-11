'''

*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
 с параметрами (характеристиками товара: название, цена, количество, единица измерения).
 Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}

'''
# Вариант 1

goods = [(1, {"название: ": "компьютер", "цена (руб.): ": 20000, "количество: ": 5, "eд.: ": "шт."}),
         (2, {"название: ": "принтер", "цена (руб.): ": 6000, "количество: ": 2, "eд.: ": "шт."}),
         (3, {"название: ": "сканер", "цена (руб.): ": 2000, "количество: ": 7, "eд.: ": "шт."})
         ]
result = {"название: ": [],
          "цена (руб.): ": [],
          "количество: ": [],
          "eд.: ": {'шт.'}
          }
answer, amount = ' ', int(input('Сколько товаров будем вводить? '))
len_list = len(goods) + 1
end = len_list + amount
while answer != 'exit':
    for i in range(len_list, end):
        goods.append((i, {"название: ": input("название: "), "цена (руб.): ": int(input("цена (руб.): ")),
                          "количество: ": int(input("количество: ")), "eд.: ": input("eд.: ")}))
    answer = input(
        'exit - выход, all - посмотреть весь список и выйти, svod - сведения для анализа,  enter - продолжить: ').lower()
    if answer == 'all':
        for elem in goods:
            print(elem)
        break
    elif answer == 'svod':
        for i, elem in enumerate(goods):
            name = elem[1]['название: ']
            result["название: "].append(name)
            price = elem[1]['цена (руб.): ']
            result["цена (руб.): "].append(price)
            quantity = elem[1]['количество: ']
            result["количество: "].append(quantity)
            units = elem[1]['eд.: ']
            result["eд.: "].add(units)

        for key, value in result.items():
            if key == "цена (руб.): ":
                result["цена (руб.): "].append(['Итого:', sum(value)])
            elif key == "количество: ":
                result["количество: "].append(['Итого:', sum(value)])
            elif key == "название: ":
                result["название: "].append(['Итого:', len(value)])
            print(key, ':', value)
        break

