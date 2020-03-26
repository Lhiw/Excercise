class Vehicle:
    licenseN = ""
    serialN = ""
    def turnonAir(self):
        print("Turn 0n : air")


class Car(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass

car1 = Car()
car1.turnonAir()
car1 = Car()
car1.turnonAir()
car1 = Car()
car1.turnonAir()