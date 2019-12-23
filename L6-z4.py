'''
4)	Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
 который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

'''

from itertools import count


class Car:
    speed = range(0, 200, 5)
    color = ['(Silver)', '(Red)', '(Green)', '(Light-Brown)', '(White-Blue)', '(Black)', '(White)', '(Orange)',
             '(Yellow)']
    name = ['Tesla', 'BMW', 'Mercedes', 'Bugatti', 'Maybach', 'lombargini', 'Range Rover', 'Nissan', 'Volkswagen']
    is_police = [True, False]
    drive = None
    boost = 0

    def go(self):
        Car.drive = True
        print('Go')

    def stop(self):
        Car.drive = False
        print('Stop')

    def turn(self):
        direction = {'w': 'Forward', 'a': 'Left', 'd': 'Right', 'z': 'Revers', 's': 'Slow'
                     }  # Руление

        while Car.drive:
            key = input('>').lower()
            if key not in direction:
                print('Кнопка на панели приборов. что-то включила или выключила. ')
                print('w - вперед, z - назад,  a - влево, d - вправо, s - тормоз')
                continue
            else:
                print(direction[key])  # a, d
                if direction[key] == 'Forward':  # w
                    if Car.boost == 0:
                        Car.go(self)
                        Car.boost += 1
                        Car.show_speed(self)
                    else:
                        print('Need to slow down ')
                elif direction[key] == 'Revers':  # z   Замедление и задний ход
                    if Car.boost == 0:
                        Car.go(self)
                        Car.boost += 1
                        Car.show_speed(self, reverse=True, R=-40)
                    else:
                        print('Need to slow down ')

                elif direction[key] == 'Slow':  # s  Замедление
                    if Car.boost == 0:
                        print('Stopped')
                    elif Car.boost > 0:
                        Car.boost -= 1
                        Car.show_speed(self, reverse=True, R=0)
        else:
            print('No movement')
            quit()  # На ручном тормозе

    def show_speed(self, max_speed=110, max_boost=boost, reverse=False, R=None):
        if Car.drive:
            for speed in Car.speed:
                if reverse == True:
                    if R == 0:
                        print('Speed =', 0, 'км/ч')
                        Car.turn(self)
                    elif R == -40:
                        print('Speed =', -40, 'км/ч')
                        Car.turn(self)
                elif speed > max_speed:
                    print('Caution! Speed =', speed)
                    Car.turn(self)
                else:
                    print('Speed =', speed, 'км/ч')
        else:
            print('Speed =', 0)


# 'Tesla', 'BMW', 'Mercedes', 'Bugatti', 'Maybach', 'lombargini', 'Range Rover', 'Nissan', 'Volkswagen'
class TownCar(Car):
    name = Car.name[7]  # 'Nissan',
    color = Car.color[2]

    def show_speed(self):
        if Car.drive:
            print('loading...')
            Car.show_speed(self, max_speed=60)
        else:
            print('Speed =', 0)


class SportCar(Car):
    name = Car.name[3]  # 'Bugatti'
    color = Car.color[1]


class WorkCar(Car):
    name = Car.name[8]  # 'Volkswagen'
    color = Car.color[3]

    def show_speed(self):
        if Car.drive:
            print('loading...')
            Car.show_speed(self, max_speed=40)
        else:
            print('Speed =', 0)


class PoliceCar(Car):
    name = Car.name[1]  # 'BMW'
    color = Car.color[4]
    Car.is_police = True


# car_1 = Car()
# print(car_1.name[5], PoliceCar.color, PoliceCar.is_police)
# car_1.go()
# car_1.turn()

car_2 = TownCar()
print(TownCar.name, TownCar.color)
car_2.go()
car_2.show_speed()
