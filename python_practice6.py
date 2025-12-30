#Swap two numbers (without temp variable)
a = int(input("a: "))
b = int(input("b: "))

a, b = b, a
print(a, b)

#output:a: 10
#b: 30
#30 10

# Swap Two Numbers Using Temp Variable
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap using temp
temp = a
a = b
b = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)

#output: Before swapping:
#a = 10
#b = 20

#After swapping:
#a = 20
#b = 10

#Palindrome Check
num = int(input("Enter a number: "))

if str(num) == str(num)[::-1]: 
    print("Palindrome")
else:
    print("Not Palindrome")
#output: Enter a number: 121
#Palindrome

#Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#output:
# Enter a number: 5
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50

#Prime Number Check
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#output: Enter a number: 7
#Prime    

#Reverse a String
s = input("Enter string: ")
print(s[::-1])

#output:Enter string: Deepa
#apeeD

#Sum of digits of a number
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)
#output:Enter a number: 3456
#Sum of digits: 18

