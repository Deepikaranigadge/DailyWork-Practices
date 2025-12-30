# function with doesn't have argument and return statement
def my_function():
  print("Hello ITD")

my_function()
my_function()
#output Hello ITD
# Hello ITD

#Function with return value
def add(a, b):
    return a + b
result = add(6, 3)
print(result)
#Output: 9

#Default parameters
def welcome(name="Guest"):
    print(f"Hello, {name}!")

welcome()
welcome("Deepika")
#output: Hello, Guest!
#Hello, Deepika!

#Intermediate Level Function Examples
def profile(name, age, country):
    print(f"{name} is {age} years old from {country}")

profile(age=25, name="John", country="India")
#output: John is 25 years old from India

#even number
def get_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

print(get_evens([1, 2, 3, 4, 5, 6]))
#output: [2, 4, 6]

#Function Returning Multiple Values
def math_ops(a, b):
    return a + b, a - b, a * b

add, sub, mul = math_ops(10, 5)
print(add, sub, mul)
#output: 15 5 50

#Advanced Level Function Examples
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
#output: 120

#Closure Create Custom Multipliers
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))
print(triple(10))
#output:20
#30

def outer(x):
    def inner(y):
        return x + y
    add10 = outer(10)
    print(add10(200))
    print(add10(400))
    print(add10(111))

# Recursion Reverse a String
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("Deepika"))
#output:akipeeD

#Decorator with function arguments
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
#output: Before function
#Hello!
#After function
