class Hero:
    def __init__(self):
        self.name="Yash"
        self.age=34
        self.numOfMovies=22
    def act(self):
        print("Yash is an actor")
h1=Hero()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()
h1.address="1st BTM Layout Banglore"#adding the value
print(h1.address)
h1.age=40#modify the value
print(h1.age)
del h1.address# delete the value
print(h1.address)

