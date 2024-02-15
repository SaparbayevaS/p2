#1
class MyClass():
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())
str = MyClass()
str.getString()
str.printString()
print()
#2
class Shape(object):
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l
    def area(self):
        return self.length*self.length
aSquare= Square(8)
print (aSquare.area())
print()
#3
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def area(self):
        return self.length*self.width
aRectangle = Rectangle(2,10)
print (aRectangle.area())
print()
#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
print()
#5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f'Deposit of {amount} accepted. New balance: {self.balance}'
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds. Withdrawal unsuccessful.'
        else:
            self.balance -= amount
            return f'Withdrawal of {amount} accepted. New balance: {self.balance}'
account = BankAccount(owner="John Doe")
print(account.deposit(1000))
print(account.withdraw(500))
print(account.withdraw(800))
print(account.balance) 
print()
#6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Original list:", numbers)
print("Prime numbers:", prime_numbers)