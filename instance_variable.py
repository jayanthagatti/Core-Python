# class TV:
#     def __init__(self):
#         self.brand="LG"
#         self.color="black"
#     def show(self):
#         print("TV is showing movies")
#         print(self.color)
# t1=TV()
# print(t1.brand)
# print(t1.color)
# t1.show()

# class Person:
#     def __init__(self):
#         self.name="shreyas"
#         self.gender="male"
#     def sing(self):
#         self.song="monica"
#         print(self.song)
# p1=Person()
# print(p1.name)
# print(p1.gender)
# p1.age=91
# p1.sing()
# print(p1.age)

class Bike:
    def __init__(self):
        self.brand="Hero"
        self.color="silver"
    def move(self):
        print("bike is riding")
        print(self)
b1=Bike()
print(b1.brand)
print(b1.color)
b1.move()
print(b1)