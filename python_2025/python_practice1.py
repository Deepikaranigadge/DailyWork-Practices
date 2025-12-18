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




