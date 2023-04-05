class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_gender(self, gender):
        self._gender = gender

# Cоздадим несколько объектов класса "Person" и вызовем некоторые методы.

person1 = Person("John", 30, "Male")
person2 = Person("Jane", 25, "Female")
person3 = Person("Anna", 15, "Female")

print(person1.get_name())        # John
print(person2.get_age())         # 25
print(person3.get_gender())      # Female
print(person3.get_name())

# Установим новые значения для атрибутов "name" и "age" объекта "person1", используя методы "set_name" и "set_age".

person1.set_name("Jack")
person1.set_age(35)

person3.set_gender("Male")

print("----------------------------")
print(person1.get_name())
print(person1.get_age())

print(person3.get_gender())

# Мы успешно создали класс "Person" с приватными атрибутами и методами "get" и "set",
# которые позволяют нам получить и установить значения этих атрибутов.
# Это может быть полезно, когда мы хотим ограничить доступ к некоторым атрибутам объекта и контролировать способ их изменения.

# Хотим создать два подкласса: "Employee" и "Student".
# Класс "Employee" будет представлять работника с определенной зарплатой,
# а класс "Student" - студента с определенным количеством курсов.
#
class Employee(Person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

# Создали класс "Employee", который наследует класс "Person". У класса "Employee" есть дополнительный атрибут "salary",
# который мы передаем в конструктор. Мы делаем этот атрибут приватным, поэтому его нельзя будет напрямую изменить извне.

class Student(Person):
    def __init__(self, name, age, gender, courses):
        super().__init__(name, age, gender)
        self.__courses = courses

    def get_courses(self):
        return self.__courses

    def set_courses(self, courses):
        self.__courses = courses

employee1 = Employee("John", 40, "Male", 50000)
student1 = Student("Jane", 20, "Female", 4)

print(employee1.get_name())  # John
print(employee1.get_age())  # 40
print(employee1.get_salary())  # 50000

print(student1.get_name())  # Jane
print(student1.get_age())  # 20
print(student1.get_courses())  # 4

# -----------------------------------------------------------------------------------------------------------------
# Каждый атрибут начинается с символа подчеркивания "_", что означает, что они являются приватными атрибутами.
# Это означает, что мы не можем получить доступ к ним напрямую извне класса.Чтобы получить доступ к приватному
# атрибуту, мы должны использовать методы "get" и "set".

# Метод "init" - это метод, который вызывается при создании объекта класса.
# Он инициализирует атрибуты объекта значениями, переданными в конструктор класса.
# Здесь мы инициализируем атрибуты "name", "age" и "gender" значениями, переданными в качестве параметров конструктора.

# Методы "get_name", "get_age" и "get_gender" - это методы,
# которые возвращают значения атрибутов "name", "age" и "gender".

# Методы "set_name", "set_age" и "set_gender" - это методы,
# которые устанавливают значения атрибутов "name", "age" и "gender".