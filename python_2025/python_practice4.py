#map with lambda

#square each number
numbers = [1,2,3,4]
result = list(map(lambda x: x*x, numbers))
print(result)
#output : [1, 4, 9, 16]

#convert list of numbers to string
nums = [10,20,30]
result = list(map(lambda n: str(n), nums))
print(result)
#output: ['10', '20', '30']

#multiply by 3
numbers = [1,2,3,4]
result = list(map(lambda x: x*3, numbers))
print(result)
#output:[3, 6, 9, 12]

#Add 5 to every element
nums = [2,4,6,8]
result = list(map(lambda n: n+5, nums))
print(result)
#output:[7, 9, 11, 13]

#Filter numbers greater than 50
numbers = [10, 55, 40, 75, 30, 90]
result = list(filter(lambda x: x > 50, numbers))
print(result)
#output: [55, 75, 90]

#Filter words whose length is more than 4
words = ["cat", "elephant", "dog", "apple", "rat"]
result = list(filter(lambda w: len(w) > 4, words))
print(result)
#output: ['elephant', 'apple']

#reduce with lambda
from functools import reduce
num2 =[1,2,3,4,5,6]
out = reduce(lambda x, y: x + y , num2)
print(out)
#output: [7, 9, 11, 13]

#find maximum number
from functools import reduce
numbers = [10, 50, 20, 90, 40]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum number:", maximum)
#output:Maximum number: 90

#Total Price in Shopping Cart
from functools import reduce
prices = [499, 999, 250, 750]
total_amount = reduce(lambda a, b: a + b, prices)
print("Total Amount:", total_amount)
#output: Total Amount: 2498

#otal Bank Balance from Transactions
from functools import reduce
transactions = [2000, -500, 1500, -300, 1000]
balance = reduce(lambda a, b: a + b, transactions)
print("Final Balance:", balance)
#output: Final Balance: 3700

