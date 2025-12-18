class Vehicle:
    pass
print("==>", Vehicle)
#output: ==> <class '__main__.Vehicle'>

class Vehicle:
    def __init__(self):
     print("hello")
car = Vehicle()
bus = Vehicle()
schooter = Vehicle()    
#Output :hello
#hello
#hello

class Vehicle:
    def __init__(self , wls):
     self.wheels = wls
car = Vehicle(4)
bus = Vehicle(6)
schooter = Vehicle(2)
print(car.wheels)
print(bus.wheels)
print(schooter.wheels)
#output: 4
#6
#2

class Vehicle:
    def __init__(self , wls):
     self.wheels = wls
     self.move = "Yes"
car = Vehicle(4)
bus = Vehicle(6)
schooter = Vehicle(2)
print(car.move)
print(bus.move)
print(schooter.move)
#output: Yes
#Yes
#Yes

class Vehicle:
   def __init__(self , brnd, yr, airbag):
      self.brand = brnd
      self.Year = yr
      self.airbag = airbag
class Car(Vehicle):
   def __init__(self, brnd, yr):
      super().__init__(brnd, yr, 6)
c = Car("Volvo", 2023)
print(c.brand)
print(c.airbag)             
#output: Volvo
#6    

#class Vehicle:
#   def __init__(self , brnd, yr, airbag):
#      self.brand = brnd
#      self.Year = yr
#     self.airbag = airbag
#class Car(Vehicle):
#   def __init__(self, brnd, yr):
#      super().__init__(brnd, yr)
#c = Car("Volvo", 2023)
#print(c.brand)
#print(c.airbag) 
#output:Vehicle.__init__() missing 1 required positional argument: 'airbag'

class Vehicle:
   def __init__(self , brnd, yr, airbag):
      self.brand = brnd
      self.Year = yr
      self.airbag = airbag

class Car(Vehicle):
   def __init__(self, brnd, yr):
      super().__init__(brnd, yr, 4)

class plane(Vehicle):
   def __init__(self, brnd, yr):
      super().__init__(brnd, yr, "NA")

car1 =Car("Volvo", 2023)
pln =plane("AirBus", 2020)
print(car1.airbag)
print(pln.airbag) 
#putout:4
#NA

class Vehicle:
    def __init__(self, brnd, yr, airbag):
        self.brand = brnd
        self.year = yr
        self.airbag = airbag

    def move(self):
        print("I move generally")

class Car(Vehicle):
    def __init__(self, brnd, yr):
        super().__init__(brnd, yr, 4)

    def move(self):
        print("I move on Road")

class Plane(Vehicle):
    def __init__(self, brnd, yr):
        super().__init__(brnd, yr, "NA")

    def move(self):
        print("I move in Air")


v1 = Vehicle("Volvo", 2023, "TBD")
car1 = Car("Volvo", 2023)
pln1 = Plane("AirBus", 2020)

v1.move()
car1.move()
pln1.move()
#output:I move generally
#I move on Road
#I move in Air

