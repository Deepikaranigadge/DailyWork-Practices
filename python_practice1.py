file1 = "Java.exe"
file2 = "java.exe"
print(file1 == file2)
#output : False

file1 ="java.exe"
file2 ="java.exe"
print(file1==file2)
#output : Ture

file1="Java.exe"
file2 ="java.exe"
print(file1.upper())
print(file2.upper())
print(file1.upper() == file2.upper())
#output: JAVA.EXE
#JAVA.EXE

file1="Java.exe"
file2 ="java.exe"
print(file1.islower())
#output: False

file1="Java.exe"
file2 ="java.exe"
print(file2.islower())
#output: Ture

name = "virat kolhi"
print(name.capitalize())
#output: Virat kolhi

name ="The home of have a good of time"
print(name.count("of"))
#output: 2

name ="The home of have a good of time"
print(name.count(" "))
#output: 7

name ="The home of have a good of time"
print(name.count("h"))
#output: 3

name ="The home of have a good of time"
print(name.endswith("time"))
#output: Ture

name ="The home of have a good of time"
print(name.endswith("good"))
#output: False

name ="The home of have a good of time"
print(name.find("good"))
#output: 19

name ="The home of have a good of time"
print(name.find("house"))
#output: -1

first_name = "Virat"
last_name = "kolhi"
full_name = first_name +" "+last_name
print(full_name)
#output:Virat kolhi

# date 30/11/25

numbers = {10, 20, 30}
print(numbers)
#output :{10, 20, 30}

numbers = {10, 20, 30}
numbers.add(40)
print(numbers)
#output: {40, 10, 20, 30}

numbers = {10, 20, 30}
numbers.update([50, 60])
print(numbers)
#output : {50, 20, 60, 10, 30}

numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)
#output: {10, 30}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
#output: {1, 2, 3, 4, 5}

a = {10, 20, 30}
b = {20, 40}
print(a.intersection(b))
#output : {20}

A = {1, 2, 3}
B = {2, 3}
print(A.difference(B))
#output : {1}

numbers = {10, 20, 30}
print(20 in numbers)
#output: True

numbers = {10, 20, 30}
for x in numbers:
    print(x)
#output : 10
#20
#30

fruits = {"apple", "banana", "orange", "grapes", "mango"}
print(fruits)
#output: {'orange', 'banana', 'apple', 'mango', 'grapes'}




