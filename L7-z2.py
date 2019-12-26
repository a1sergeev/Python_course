'''
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.

'''
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def price(self):
        print(f" (Цена)")

    @abstractmethod
    def code(self):
        print(f" (Артикул)")

    def __init__(self, title="No_name"):
        self.title = title


class Coat(Clothes):
    def __init__(self, title="No_name"):  # размер 50
        super().__init__(title)
        print(self.title)

    def price(self):
        print(f" [Цена: 400000]")

    def code(self):
        print(f" [Артикул: C0011]")


class Suit(Clothes):
    def __init__(self, title="No_name"):
        super().__init__(title)
        print(self.title)

    def price(self):
        print(f" [Цена: 300000]")

    def code(self):
        print(f" [Артикул: S0011]")


class Calc:
    def __init__(self, param_1=0, param_2=0, V=0, H=0):
        self.param_1 = param_1
        self.param_2 = param_2
        self.V = int(V)
        self.H = int(H)

    @property
    def calculator(self): # V - размер (для пальто) и H - рост (для костюма)
        if self.V:
            self.param_1 = round((self.V / 6.5 + 0.5), 2)
            print(f'Расход = {self.V / 6.5 + 0.5:.2f} ')
        elif self.H:
            self.param_2 = round((2 * self.H + 0.3), 2)
            print(f'Расход = {2 * self.H + 0.3:.2f} ')

        return self.param_1 + self.param_2


garb_1 = Coat('BRIONI')  #
garb_1.code()
garb_1.price()
garb_1 = Calc(V=50)

garb_2 = Suit('Cartier')
garb_2.code()
garb_2.price()
garb_2 = Calc(H=48)

print('Суммарный расход = ', garb_1.calculator + garb_2.calculator)
