class Fan:
    def __init__(self):
        self.brand="usha"
        self.color="white"
        self.wings=3
        self.cost=2000
    def on(self):
        print("fan is on")
    def rotate(self):
        print("fan is rotating")
    def off(self):
        print("fan is off")
f1=Fan()
print(f1.brand)
print(f1.color)
print(f1.wings)
print(f1.cost)
f1.on()
f1.rotate()
f1.off()