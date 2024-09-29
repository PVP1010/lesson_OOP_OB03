class Engine:
    def __init__(self, horsepower):                   # Инициализация экземпляра класса Engine с атрибутом мощности (horsepower)
        self. horsepower = horsepower
class Car:
    def __init__(self, model, engine_horsepower):     # Инициализация экземпляра класса Car с атрибутом модели (model)
        self.model = model                            # Инициализация экземпляра класса Engine внутри класса Car
        self. engine = Engine (engine_horsepower)     # Это пример композиции, где Car содержит объект Engine

car = Car("Toyota", 268)        # Создание объекта car класса Car с моделью "Toyota" и мощностью двигателя 268 л.с.


class Engine():

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()


class Car():
    def __init__(self):
        self.engine = Engine
my_Car = Car()

my_Car.start()