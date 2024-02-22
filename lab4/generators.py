#1
def generator_squares(n):
    squares = [i * i 
               for i in range(1, n + 1)]
    return squares
n = int(input())
result = generator_squares(n)
print(result)
print()
#2
def even_numbers_generator(n):
    numbers = [i
             for i in range(0, n, 2)]
    return numbers
n = int(input())
res = even_numbers_generator(n)
result_str = ', '.join(str(num) 
                       for num in res)
print(result_str)
print()
#3
def divisible(n):
    div = [i
               for i in range(0, n + 1)
               if i % 3 == 0 and i % 4 == 0]
    return div
n = int(input())
result = divisible(n)
print(result)
print()
#4
def squares(a, b):
    square = [i * i 
               for i in range(a, b + 1)]
    return square
a = int(input())
b = int(input())
result = squares(a, b)
print(result)
print()
#5
def numbers(n):
    num = [i
               for i in range(n, 0, -1)]
    return num
n = int(input())
result = numbers(n)
print(result)
print()