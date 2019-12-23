'''
1)	Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
from itertools import cycle
import time


class TrafficLight:
    __color = ['Red', 'Red', 'Yellow', 'Yellow', 'Green', 'Green', 'Yellow', 'Yellow']
    __status = ['On', 'Off']
    __time = [7, 1, 2, 1, 15, 1, 2, 1]

    def running(self):
        iter_color = cycle(TrafficLight.__color)
        iter_status = cycle(TrafficLight.__status)
        iter_time = cycle(TrafficLight.__time)
        support = 8409600
        while True:
            support -= 1
            print(next(iter_color), next(iter_status))
            time.sleep(next(iter_time))
            if support == 0:
                print('SMS: GIBDD: Требуется тех. обслуживание светофора №13 на ул. Вязов')
                print(TrafficLight.__color[2], TrafficLight.__status[0])
                break


Light = TrafficLight()
Light.running()

'''
            #красный-вкл 7сек желтый-вкл 2сек красн-выкл желтый-выкл зеленный-вкл 10сек зел_моргающий 2сек зел-выкл желтый-вкл 2сек желтый-выкл
            print(TrafficLight.__color[0], TrafficLight.__status[0]) #кр
            time.sleep(TrafficLight.__time[0]) #7

            print(TrafficLight.__color[2], TrafficLight.__status[0]) #жел
            time.sleep(TrafficLight.__time[2]) #2
            print(TrafficLight.__color[0], TrafficLight.__status[1])  # кр_выкл
            print(TrafficLight.__color[2], TrafficLight.__status[1]) #жел_выкл

            print(TrafficLight.__color[4], TrafficLight.__status[0]) #зел
            time.sleep(TrafficLight.__time[4])#10
            print(TrafficLight.__color[4], TrafficLight.__status[2]) #морг зел
            time.sleep(TrafficLight.__time[2])#2
            print(TrafficLight.__color[4], TrafficLight.__status[1])  # зел_выкл
            
            print(TrafficLight.__color[2], TrafficLight.__status[0]) #жел
            time.sleep(TrafficLight.__time[2]) #2
            print(TrafficLight.__color[2], TrafficLight.__status[1]) #жел_выкл
            

Light = TrafficLight()
Light.running()

'''
