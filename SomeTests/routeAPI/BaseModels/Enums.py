from enum import Enum



class type_of_point(Enum):
    stop = 'stop'              #  начальная/конечная точка маршрута (прямой путь до дороги, игнорирующий препятствия)
    walking = 'walking'        #  начальная/конечная точка маршрута (пешеходный путь до дороги)
    pref = 'pref'              #  промежуточная точка маршрута


class type_of_transport(Enum):
    car = 'car'                #   автомобиль
    truck = 'truck'            #   грузовой транспорт
    emergency = 'emergency'    #   кстренные службы
    bicycle = 'bicycle'        #   велосипед
    taxi = 'taxi'              #   такси
    pedestrian = 'pedestrian'  #   пешеход

class type_of_route_mode(Enum):
    fastest = 'fastest'        #   кратчайший по времени с учетом текущих пробок или с учётом статистических данных по пробкам
    shortest = 'shortest'      #   кратчайший по расстоянию без учета пробок


class type_of_traffic_mode(Enum):
    jam = 'jam'                #   использовать данные о текущих пробках
    statistics = 'statistics'  #   использовать статистические данные о пробках


class output(Enum):
    summary = 'summary'        #   упрощенная выдача, в ответе только время и длина маршрута
    detailed = 'detailed'      #   полная выдача с геометрией маршрута






