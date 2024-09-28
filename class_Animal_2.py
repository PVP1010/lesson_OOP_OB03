import pickle  # Импортируем модуль pickle для сериализации объектов в файл и их десериализации из файла.

class Animal():                     # Определяем класс Animal как базовый класс для всех животных.
    def __init__(self, name, age):  # Инициализатор класса, который принимает имя и возраст животного.
        self.name = name          # Устанавливаем атрибут name для объекта.
        self.age = age            # Устанавливаем атрибут age для объекта.

    def make_sound(self):         # Метод, который должен быть реализован в дочерних классах для издаваемого звука.
        pass

    def eat(self):                # Метод, возвращающий строку, указывающую, что животное ест.
        return f"{self.name} ест."

class Bird(Animal):               # Определяем класс Bird, наследующий от Animal.
    def __init__(self, name, age, wing_span):  # Инициализатор для класса Bird.
        super().__init__(name, age)  # Вызываем инициализатор базового класса.
        self.wing_span = wing_span  # Устанавливаем размах крыльев для птицы.

    def make_sound(self):  # Переопределяем метод make_sound для птиц.
        return f"{self.name} щебечет."


class Mammal(Animal):  # Определяем класс Mammal, наследующий от Animal.
    def __init__(self, name, age, fur_color):  # Инициализатор для класса Mammal.
        super().__init__(name, age)  # Вызываем инициализатор базового класса.
        self.fur_color = fur_color  # Устанавливаем цвет шерсти для млекопитающего.

    def make_sound(self):  # Переопределяем метод make_sound для млекопитающих.
        return f"{self.name} ревёт."


class Reptile(Animal):  # Определяем класс Reptile, наследующий от Animal.
    def __init__(self, name, age, scale_type):  # Инициализатор для класса Reptile.
        super().__init__(name, age)  # Вызываем инициализатор базового класса.
        self.scale_type = scale_type  # Устанавливаем тип чешуи для рептилии.

    def make_sound(self):  # Переопределяем метод make_sound для рептилий.
        return f"{self.name} шипит."


def animal_sound(animals):  # Функция, которая принимает список животных и выводит их звуки.
    for animal in animals:  # Проходим по каждому животному в списке.
        print(animal.make_sound())  # Вызываем метод make_sound и выводим результат.


class Zoo:  # Определяем класс Zoo для представления зоопарка.
    def __init__(self):  # Инициализатор для класса Zoo.
        self.animals = []  # Создаем пустой список для хранения животных.
        self.staff = []  # Создаем пустой список для хранения персонала.

    def add_animal(self, animal):  # Метод для добавления животного в зоопарк.
        self.animals.append(animal)  # Добавляем животное в список animals.

    def add_staff(self, person):  # Метод для добавления сотрудника в зоопарк.
        self.staff.append(person)  # Добавляем сотрудника в список staff.

    def save_to_file(self, filename):  # Метод для сохранения состояния зоопарка в файл.
        with open(filename, 'wb') as file:  # Открываем файл для записи в бинарном режиме.
            pickle.dump(self, file)  # Сериализуем объект зоопарка и записываем в файл.

    @staticmethod
    def load_from_file(filename):  # Статический метод для загрузки зоопарка из файла.
        try:
            with open(filename, 'rb') as file:  # Открываем файл для чтения в бинарном режиме.
                return pickle.load(file)  # Десериализуем объект зоопарка из файла.
        except FileNotFoundError:  # Если файл не найден, создаем новый объект Zoo.
            return Zoo()

# Импортируем классы и функции из нашего модуля
# from zoo_module import Animal, Bird, Mammal, Reptile, Zoo  # Предположим, что наш код находится в файле zoo_module.py

# Создаем экземпляры животных
воробей = Bird("Воробей", 2, "Средний")  # Создаем птицу с размахом крыльев
лев = Mammal("Лев", 5, "Золотистый")     # Создаем млекопитающее с цветом шерсти
ящерица = Reptile("Ящерица", 1, "Гладкая")  # Создаем рептилию с типом чешуи

# Создаем зоопарк
зоопарк = Zoo()

# Добавляем животных в зоопарк
зоопарк.add_animal(воробей)
зоопарк.add_animal(лев)
зоопарк.add_animal(ящерица)

# Вызываем звуки всех животных в зоопарке
print("Звуки животных в зоопарке:")
animal_sound(зоопарк.animals)

# Кормим всех животных в зоопарке
print("\nКормление животных в зоопарке:")
for animal in зоопарк.animals:
    print(animal.eat())

# Сохраняем состояние зоопарка в файл
файл_зоопарка = "zoo_data.pkl"
зоопарк.save_to_file(файл_зоопарка)
print(f"\nСостояние зоопарка сохранено в файл {файл_зоопарка}.")

# Загружаем состояние зоопарка из файла
загруженный_зоопарк = Zoo.load_from_file(файл_зоопарка)
print("\nЗагруженное состояние зоопарка:")

# Вызываем звуки всех животных в загруженном зоопарке
animal_sound(загруженный_зоопарк.animals)

# Проверяем, что загруженные данные совпадают с оригинальными
print("\nПроверка совпадения загруженных данных:")
for original, loaded in zip(зоопарк.animals, загруженный_зоопарк.animals):
    assert original.name == loaded.name, "Имена не совпадают"
    assert original.age == loaded.age, "Возраст не совпадает"
    print(f"{original.name} загружен правильно.")

