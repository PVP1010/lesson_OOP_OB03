import pickle  # Импортируем модуль pickle для сериализации объектов в файл и их десериализации из файла.

class Animal():                 # Определяем класс Animal как базовый класс для всех животных.
    def init(self, name, age):  # Инициализатор класса, который принимает имя и возраст животного.
        self.name = name        # Устанавливаем атрибут name для объекта.
        self.age = age          # Устанавливаем атрибут age для объекта.

    def make_sound(self):       # Метод, который должен быть реализован в дочерних классах для издаваемого звука.
        pass

    def eat(self):                                 # Метод, возвращающий строку, указывающую, что животное ест.
        return f"{self.name} ест."

class Bird(Animal):                                # Определяем класс Bird, наследующий от Animal.
    def init(self, name, age, wing_span):          # Инициализатор для класса Bird.
        super().init(name, age)                    # Вызываем инициализатор базового класса.
        self.wing_span = wing_span                 # Устанавливаем размах крыльев для птицы.

    def make_sound(self):                          # Переопределяем метод make_sound для птиц.
        return f"{self.name} щебечет."

class Mammal(Animal):                              # Определяем класс Mammal, наследующий от Animal.
    def init(self, name, age, fur_color):          # Инициализатор для класса Mammal.
        super().init(name, age)                    # Вызываем инициализатор базового класса.
        self.fur_color = fur_color                 # Устанавливаем цвет шерсти для млекопитающего.

    def make_sound(self):                          # Переопределяем метод make_sound для млекопитающих.
        return f"{self.name} ревёт."

class Reptile(Animal):                             # Определяем класс Reptile, наследующий от Animal.
    def init(self, name, age, scale_type):         # Инициализатор для класса Reptile.
        super().init(name, age)                    # Вызываем инициализатор базового класса.
        self.scale_type = scale_type               # Устанавливаем тип чешуи для рептилии.

    def make_sound(self):                          # Переопределяем метод make_sound для рептилий.
        return f"{self.name} шипит."


def animal_sound(animals):                         # Функция, которая принимает список животных и выводит их звуки.
    for animal in animals:                         # Проходим по каждому животному в списке.
        print(animal.make_sound())                 # Вызываем метод make_sound и выводим результат.

class Zoo:                                         # Определяем класс Zoo для представления зоопарка.
    def init(self):                                # Инициализатор для класса Zoo.
        self.animals = []                          # Создаем пустой список для хранения животных.
        self.staff = []                            # Создаем пустой список для хранения персонала.

    def add_animal(self, animal):                  # Метод для добавления животного в зоопарк.
        self.animals.append(animal)                # Добавляем животное в список animals.

    def add_staff(self, person):                   # Метод для добавления сотрудника в зоопарк.
        self.staff.append(person)                  # Добавляем сотрудника в список staff.

    def save_to_file(self, filename):              # Метод для сохранения состояния зоопарка в файл.
        with open(filename, 'wb') as file:         # Открываем файл для записи в бинарном режиме.
            pickle.dump(self, file)                # Сериализуем объект зоопарка и записываем в файл.

    @staticmethod
    def load_from_file(filename):                  # Статический метод для загрузки зоопарка из файла.
        try:
            with open(filename, 'rb') as file:     # Открываем файл для чтения в бинарном режиме.
                return pickle.load(file)           # Десериализуем объект зоопарка из файла.
        except FileNotFoundError:                  # Если файл не найден, создаем новый объект Zoo.
            return Zoo()

class ZooKeeper:                                   # Определяем класс ZooKeeper для представления смотрителя зоопарка.
    def init(self, name):                          # Инициализатор для класса ZooKeeper.
        self.name = name                           # Устанавливаем имя смотрителя.

    def feed_animal(self, animal):                 # Метод, описывающий кормление животного.
        return f"{self.name} кормит {animal.name}."

class Veterinarian:                                 # Определяем класс Veterinarian для представления ветеринара.
    def init(self, name):                           # Инициализатор для класса Veterinarian.
        self.name = name                            # Устанавливаем имя ветеринара.

    def heal_animal(self, animal):                  # Метод, описывающий лечение животного.
        return f"{self.name} лечит {animal.name}."

# Пример использования
if __name__ == "__main__":  # Проверяем, что скрипт выполняется как основная программа.
    # Попробуем загрузить зоопарк из файла, если он существует
    zoo = Zoo.load_from_file('zoo_data.pkl')

    # Если зоопарк пуст, добавим животных и сотрудников
    if not zoo.animals:  # Проверяем, есть ли животные в зоопарке.
        popugay = Bird("Попугай", "2 года", "Средний")  # Создаем объект птицы.
        lev = Mammal("Лев", "5 лет", "Золотистый")  # Создаем объект млекопитающего.
        zmeya = Reptile("Змея", "3 года", "Гладкая")  # Создаем объект рептилии.

        zoo.add_animal(popugay)  # Добавляем птицу в зоопарк.
        zoo.add_animal(lev)  # Добавляем млекопитающего в зоопарк.
        zoo.add_animal(zmeya)  # Добавляем рептилию в зоопарк.

    if not zoo.staff:  # Проверяем, есть ли сотрудники в зоопарке.
        sidorov = ZooKeeper("Василий")  # Создаем объект смотрителя.
        vet = Veterinarian("Др.Иванов")  # Создаем объект ветеринара.

        zoo.add_staff(sidorov)  # Добавляем смотрителя в зоопарк.
        zoo.add_staff(vet)  # Добавляем ветеринара в зоопарк.

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)  # Вызываем функцию для вывода звуков всех животных.

    # Демонстрация методов сотрудников
    for staff in zoo.staff:  # Проходим по каждому сотруднику в зоопарке.
        if isinstance(staff, ZooKeeper):  # Проверяем, является ли сотрудник смотрителем.
            print(staff.feed_animal(lev))  # Выводим результат кормления льва.
        elif isinstance(staff, Veterinarian):  # Проверяем, является ли сотрудник ветеринаром.
            print(staff.heal_animal(popugay))  # Выводим результат лечения попугая.

    # Сохраняем текущее состояние зоопарка в файл
    zoo.save_to_file('zoo_data.pkl')  # Сериализуем и сохраняем объект зоопарка в файл.