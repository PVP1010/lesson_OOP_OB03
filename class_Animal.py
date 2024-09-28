class Animal():                                   # Базовый класс Animal
    def __init__(self, name, age):                # Инициализация общих атрибутов для всех животных
        self.name = name
        self.age = age

    def make_sound(self):                         # Общий метод для издания звука, переопределяется в подклассах
        pass

    def eat(self):                                # Метод, показывающий, что животное ест
        return f"{self.name} ест."

class Bird(Animal):                               # Подкласс Bird
    def __init__(self, name, age, wing_span):     # Инициализация с учетом специфического атрибута wing_span
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):                         # Переопределение метода make_sound для птиц
        return f"{self.name} щебечит."

class Mammal(Animal):                             # Подкласс Mammal
    def __init__(self, name, age, fur_color):     # Инициализация с учетом специфического атрибута fur_color
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):                         # Переопределение метода make_sound для млекопитающих
        return f"{self.name} ревёт."

class Reptile(Animal):                            # Подкласс Reptile
    def __init__(self, name, age, scale_type):    # Инициализация с учетом специфического атрибута scale_type
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):                         # Переопределение метода make_sound для рептилий
        return f"{self.name} шипит."


def animal_sound(animals):                        # Функция для демонстрации полиморфизма
    for animal in animals:                        # Вызывает метод make_sound для каждого животного в списке
        print(animal.make_sound())

class Zoo:                                        # Класс Zoo, использующий композицию
    def __init__(self):                           # Инициализация списков для животных и сотрудников
        self.animals = []
        self.staff = []

    def add_animal(self, animal):                 # Метод для добавления животного в зоопарк
        self.animals.append(animal)

    def add_staff(self, person):                  # Метод для добавления сотрудника в зоопарк
        self.staff.append(person)

# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):                            # Инициализация с именем смотрителя
        self.name = name

    def feed_animal(self, animal):                       # Метод для кормления животного
        return f"{self.name} кормит {animal.name}."

class Veterinarian:                                      # Класс Veterinarian
    def __init__(self, name):                            # Инициализация с именем ветеринара
        self.name = name

    def heal_animal(self, animal):                        # Метод для лечения животного
        return f"{self.name} лечит {animal.name}."

# Пример использования
if __name__ == "__main__":
    # Создание экземпляров животных
    popugay = Bird("Попугай", "2 года", "Средний")
    lev = Mammal("Лев", "5 лет", "Золотистый")
    zmeya = Reptile("Змея", "3 года", "Гладкая")

    print(popugay)


    # Демонстрация полиморфизма
    animals = [popugay, lev, zmeya]
    animal_sound(animals)

    # Создание зоопарка и добавление животных
    zoo = Zoo()
    zoo.add_animal(popugay)
    zoo.add_animal(lev)
    zoo.add_animal(zmeya)

    # Создание сотрудников и добавление их в зоопарк
    sidorov = ZooKeeper("Василий")
    vet = Veterinarian("Др.Иванов")
    zoo.add_staff(sidorov)
    zoo.add_staff(vet)

    # Демонстрация методов сотрудников
    print(sidorov.feed_animal(lev))
    print(vet.heal_animal(popugay))