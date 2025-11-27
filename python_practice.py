print("Good Day")
#output: Good Day

x= 10
y= 20
print(x+y)
#output: 30

pi =3.142
r=2
print(2*pi*r)
#output:12.568

x, y = 10, 20
print(y)
print(x)
#output:20
10

x =10,20
print(x)
#output:(10, 20)

x= 10,20,30
print(x)
#output:(10, 20, 30)

x=10
x="India"
print(x)
#output:India

x=10
x="India"
x=[20, 40]
print(x)
#output:[20, 40]

x="Beginner"
print(x)
x="good"
x="expert"
#output:Beginner

x="Beginner"
print(x)
x="Good"
print(x)
x="Expert"
print(x)
#output:Beginner Good Expert

person1 = person2 = person3 = "Expert"
print(person1)
#output:Expert Expert Expert

person1 = person2 = person3 = "Expert"
print(person1)
print(person2)
print(person3)
#output:('Expert', 'Good')
#('Expert', 'Good')
#('Expert', 'Good')

person1 = person2 = person3 = "Expert" , "Good"
print(person1)
print(person2)
print(person3)
#output:

person1, person2, person3 = "Expert" , "Good", "Good"
print(person1)
print(person2)
print(person3)
#output:Expert
#Good
#Good

#person1, person2, person3 = "Expert" , "Good"
#print(person1)
#print(person2)
#print(person3)
#output: ERROE

print("\n\n")
#output: NEW LINE

x=20
print("value of x is ", x)
#output:value of x is  20

x=            20
print("value of x is ", x)
#output:value of x is  20


#              Date 27 /11 /25
number1 = 10
print(type(number1))
#output :<class 'int'>

number1 = 10.4
print(type(number1))
#output : <class 'float'>

number1 = 10.4 + 20j
print(type(number1))
#output: <class 'complex'>

number1 = 10.4 + 20
print(type(number1))
#output: <class 'float'>

number1 = 10 + 20.4
print(type(number1))
#output: <class 'float'>

number1 = 10.4
print(type(number1))
#output: <class 'float'>

str1 = ''
print(type(str1))
# output: <class 'str'>

str1 =""
print(type(str1))
# output: <class 'str'>

str1 = ''' '''
print(type(str1))
# output: <class 'str'>

str1 = ''''''
print(type(str1))
# output: <class 'str'>

str1 = str()
print(type(str1))
# output: <class 'str'>

str1 = str(123)
print(type(str1))
# output: <class 'str'>

first_name = 'virat'
print(len(first_name))
#output : 5

first_name = 'virat kolhi'
print(len(first_name))
#output : 11

first_name = ''
print(len(first_name))
#output : 0

first_name = ' '
print(len(first_name))
#output : 1

first_name = 'VIRAT'
print(len(first_name))
print("The value at position 0", first_name[0])
print("The value at position 4", first_name[4])
#output :The value at position 0 V
#        The value at position 4 T

#first_name = 'VIRAT'
#print("The value at position 5", first_name[5])
# error string index out of range

first_name = 'VIRAT'
print(first_name[5-1])
#output : T


