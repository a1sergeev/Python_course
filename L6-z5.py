'''
5)	Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    title = 'Stationery '

    def draw(self):
        print('Запуск отрисовки: ', end=' ')


class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('Pen ')

class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('Pencil ')

class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('Handle ')


#h = Stationery()
#h.draw()

h = Pen()
h.draw()

h = Pencil()
h.draw()

h = Handle()
h.draw()
