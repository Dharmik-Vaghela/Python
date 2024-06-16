class vehicle:
    def v1(self):
        pass

class bus(vehicle):
    def v1(self):
        print("Bus")

class car(vehicle):
    def v1(self):
        print("Car")

b=bus()
c=car()
b.v1()
c.v1()