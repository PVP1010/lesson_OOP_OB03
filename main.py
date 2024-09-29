# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# 2. и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# 3. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод
# 4. `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# 5. Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например,
# 6. `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).



class Animal():                                   # Базовый класс Animal
    def __init__(self, name, age):                # Инициализация общих атрибутов для всех животных
        self.name = name
        self.age = age

    def make_sound(self):                         # Общий метод для издания звука, переопределяется в подклассах
        pass

    def eat(self):                                # Метод, показывающий, что животное ест
        print(f"{self.name} кушает")
#        return f"{self.name} ест."


    # НАСЛЕДОВАНИЕ ....................................................................

class Bird(Animal):                               # Подкласс Bird
    def make_sound(self):                         # Переопределение метода make_sound для птиц
        print("чирик чирик")
#        return f"{self.name} щебечит."

class Mammal(Animal):                             # Подкласс Mammal
    def make_sound(self):                         # Переопределение метода make_sound для млекопитающих
        print("рычит")
#        return f"{self.name} ревёт."

class Reptile(Animal):                            # Подкласс Reptile
    def make_sound(self):                         # Переопределение метода make_sound для рептилий
        print("шипит")
#        return f"{self.name} шипит."


    # ПОЛИМОРФИЗМ ........................................................................

def animal_sound(animals):                        # Функция для демонстрации полиморфизма
    for animal in animals:                        # Вызывает метод make_sound для каждого животного в списке
        animal.make_sound()
#        print(animal.make_sound())

   # методы для добавления животных и сотрудников в зоопарк ...............................

class Zoo():                                        # Класс Zoo, использующий композицию
    def __init__(self):                           # Инициализация списков для животных и сотрудников
        self.animals = []
        self.staff = []

    def add_animal(self, animal):                 # Метод для добавления животного в зоопарк
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_staff(self, person):                  # Метод для добавления сотрудника в зоопарк
        self.staff.append(person)
        print(f"Новый сотрудник {person} добавлен в зоопарк")

   # классы сотрудников .....................................................................

# Класс ZooKeeper
class ZooKeeper():                                       # Смотритель зоопарка
    def feed_animal(self, animal):                       # Метод для кормления животного
        print(f"Сотрудник кормит {animal.name}")
#        return f"{self.name} кормит {animal.name}."

class Veterinarian():                                      # Класс ветеринар
    def heal_animal(self, animal):                        # Метод для лечения животного
        print(f"Ветеринар лечит {animal.name}")
#        return f"{self.name} лечит {animal.name}."

# Пример использования

     # Объекты классов животных
bird1 = Bird("Птица", 1)
mammal1 = Mammal("Собака", 2)
reptile1 = Reptile("Змея", 3)

     # Объект класа зоопарк
zoo = Zoo()

     # Объект класса Смотритель зоопарка
keeper = ZooKeeper()

     # Объект класа ветеринар
veterinarian = Veterinarian()

     # добавляем животных в зоопарк
zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

    # добавляем сотрудников в зоопарк
zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)

keeper.feed_animal(bird1)
veterinarian.heal_animal(mammal1)