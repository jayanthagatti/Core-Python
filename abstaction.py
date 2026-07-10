from abc import ABC,abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("dog")
class Cat(Animal):
    def sound(self):
        print("cat")
d1=Dog()
c1=Cat()
d1.sound()
c1.sound()