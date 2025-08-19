
class Laptop:
    def __init__(self):
        self.brand="hp"
    
    def display(self):
        print("laptop is displaying")
    
    @staticmethod
    def execute():
        print("laptop is executing python progrmas")

    @classmethod
    def update(cls):
        print("laptop updated")

l1=Laptop()
l1.display()
# l1.execute()
# l1.update()
Laptop.execute()
Laptop.update()