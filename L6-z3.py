'''
3)	Реализовать базовый класс Worker (работник),
 в котором определить атрибуты: name, surname, position (должность), income (доход).
 Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
 Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    name = 'Иван'
    surname = 'Иванов'
    position = 'Директор'
    wage = 0
    bonus = 0
    _income = {"wage": wage,
               "bonus": bonus
               }

    def __init__(self, name, surname, position):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position


class Position(Worker):
    def get_full_name(self):
        print('Cотрудник = ', Worker.surname, Worker.name, Worker.position)

    def get_total_income(self):
        Worker._income["wage"] = int(input("wage: "))
        Worker._income["bonus"] = int(input("bonus: "))
        print('Дохода с учетом премии = ', Worker._income["wage"] + Worker._income["bonus"], '\n')


person1 = Position('Валентина', 'Петрова', 'Кассир')
person1.get_full_name()
person1.get_total_income()

person2 = Position('Петр', 'Петров', 'Бухгалтер')
person2.get_full_name()
person2.get_total_income()

person3 = Position(position='Директор', surname='Иванов', name='Иван')
person3.get_full_name()
person3.get_total_income()