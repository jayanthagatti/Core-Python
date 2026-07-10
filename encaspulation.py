class Car:
    def __init__(self):
        self.color="red"
    def __move(self):
        print("car is moving")
    def helper(self):
        self.__move()
c1=Car()
c1.helper()