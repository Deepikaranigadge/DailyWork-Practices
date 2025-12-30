square = lambda num1: num1 * num1
print(square)
#output: <function <lambda> at 0x0000017DB769FAB0>


square = lambda num1: num1 * num1
print(10)
#output:10


square = lambda num1: num1 * num1
print(square(12))
#output:144


#add two numbers
add = lambda num1, num2: num1+ num2
print(add(20,30))
#output:50


#add = lambda num1, num2: num1+ num2, print("ok")
#print(add(20,30))
#output:TypeError: 'tuple' object is not callable


def power(x):
    return lambda y: y * x
square= power(2)
cube = power(3)
print(square)
print(cube)

#output<function power.<locals>.<lambda> at 0x000001EF6E023950>        
#<function power.<locals>.<lambda> at 0x000001EF6DFAFAB0> 

lst1 = [2,4,6,12,15,19]
out =[i * i for i in lst1]
print(out)
#output: [4, 16, 36, 144, 225, 361]

#map with lambda
lst1 = [2,4,6,12,15,19]
out_map = map(lambda num1: num1 * num1, lst1)
out =list(out_map)
print(out)
#output: [4, 16, 36, 144, 225, 361]

#filter with lambda

people = [12,3,5,21,50,45,36,29,18,17]
out =list(filter(lambda num1: num1 >= 18, people))
print(out)
#output:[21, 50, 45, 36, 29, 18]


people = [12,3,5,21,50,45,36,29,18,17]
out =tuple(filter(lambda num1: num1 >= 18, people))
print(out)
#output: (21, 50, 45, 36, 29, 18)


people = [12,3,5,21,50,45,36,29,18,17]
out =set(filter(lambda num1: num1 >= 18, people))
print(out)
#output: {36, 45, 50, 18, 21, 29}


people = [12,3,5,21,50,45,36,29,18,17]
out = [i for i in people if i > 17]
print(out)
#output:[21, 50, 45, 36, 29, 18]

import os
print((os.listdir()))
#output: ['first.py', 'python_practice.py', 'python_practice1.py', 'python_practice2.py', 'python_practice3.py']

import os 
out = list(map(lambda x : "text_" + x, os.listdir()))
print(out)
#output:['text_first.py', 'text_python_practice.py', 'text_python_practice1.py', 'text_python_practice2.py', 'text_python_practice3.py']
