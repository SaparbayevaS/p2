#1
import math
def mult_list(numbers):
    return math.prod(numbers)
list = [2, 3, 4, 5]
print(mult_list(list))
print()
#2
def counter(string):
    upper_count = sum (1 for char in string
                      if char.isupper())
    lower_count = sum (1 for char in string 
                       if char.islower())
    return upper_count, lower_count
str = input("str: ")
print(counter(str))
print()
#3
def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string 
                             if char.isalnum())
    return cleaned_string == ''.join(reversed(cleaned_string))
str = input("str: ")
if is_palindrome(str):
    print("Palindrome")
else:
    print("Not palindrome")
print()
#4
import time
def calculate_square_root():
    number = float(input("number: "))
    delay_ms = int(input("delay: "))
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    return number, delay_ms, result
number, delay, result = calculate_square_root()
print(f"Square root of {number} after {delay} milliseconds: {result}")
print()
#5
def all_true(tuple_to_check):
    return all(tuple_to_check)
my_tuple = (True, True, True)
result = all_true(my_tuple)
print(result)