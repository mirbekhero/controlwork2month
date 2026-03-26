### 1. Инкапсуляция
class Person:
    def __init__(self,age):
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        self.__age = new_age
        if new_age < 0:
            self.__age = 0
            print("Ошибка возраст не может быть отрицательным",self.__age)

        else:
            self.__age = new_age
p=Person(20)
p.set_age(25)
print(p.get_age())
p.set_age(-5)

### 2. Наследование
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "I am an animal"
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"
dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.name, dog.speak())
print(cat.name, cat.speak())

### 3. Полиморфизм
class Vehicle:
    def move(self):
        return "Vehicle is moving"
class Car(Vehicle):
    def move(self):
        return "Car is moving"
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is moving"
def move(vehicle):
    return vehicle.move()
car = Car()
bicycle = Bicycle()
print(car.move())
print(bicycle.move())
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Restangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
rect=Restangle(10,5)
circle=Circle(7)
print(rect.area())
print(circle.area())

