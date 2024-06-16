class vehicle:
    def v1(self):
        print("Bus")

class car(vehicle):
    def c1(self):
        print("Car")

c1=car()
c1.v1()
c1.c1()