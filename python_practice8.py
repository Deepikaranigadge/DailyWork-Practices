#Class & Object Example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Riya", 21)
print(s.name)
print(s.age)
# output:Riya
#21

#Encapsulation Example (Private Variable)
class Bank:
    def __init__(self, balance):
        self.__balance = balance       # private variable

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

b = Bank(1000)
print(b.deposit(500))
#output:1500

#Abstraction Example
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class UPI(Payment):
    def make_payment(self, amount):
        print(f"Paid ₹{amount} using UPI")

p = UPI()
p.make_payment(250)

#output: Paid ₹250 using UPI

#Inheritance Example
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

d = Dog()
d.eat()

#output: Animal is eating

#Polymorphism Method Overriding
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 5 * 5

s = Square()
print(s.area())
#output: 25

#Method Overloading
class Math:
    def add(self, a, b, c=0):
        return a + b + c

m = Math()
print(m.add(5, 10))
print(m.add(5, 10, 15))
 
 #output:15
#20


