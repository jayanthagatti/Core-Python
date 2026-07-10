class Plane:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")

class Passenger(Plane):
    def land(self):
        print("plane is landing")

class Cargo(Plane):
    def land(self):
        print("plane is landing")

class Fighter(Plane):
    def land(self):
        print("plane is landing")

p1=Passenger()
c1=Cargo()
f1=Fighter()

def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
allowplane(p1)
allowplane(c1)
allowplane(f1)