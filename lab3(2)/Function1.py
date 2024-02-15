#1
def grams_to_ounces():
    grams = float(input("grams: "))
    ounces = 28.3495231 * grams
    print(f" {grams} grams - {ounces:.2f} ounces")
grams_to_ounces()
print()
#2
def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f"{fahrenheit} fahrenheit - {celsius:.2f} celsius.")
fahrenheit_to_celsius()
print()
#3
def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if (2 * c + 4 * r) == numlegs:
            return c, r
num_heads = 35
num_legs = 94
solution = solve(num_heads, num_legs)
if solution:
    chickens, rabbits = solution
    print(f"{chickens} chickens and {rabbits} rabbits")
print()
#4
def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return list(filter(is_prime, numbers))
numbers_list = [2, 5, 8, 11, 14, 17, 20, 23]
prime_numbers = filter_prime(numbers_list)
print(numbers_list)
print(prime_numbers)
print()
#5
from itertools import permutations
def permutations_of_string():
    str = input("String: ")
    perms = [''.join(p) for p in permutations(str)]
    print(perms)
permutations_of_string()
print()
#6
def reverse_words():
    str = input("String: ")
    words = str.split()
    reversed_sentence = ''.join(reversed(words))
    return reversed_sentence
result = reverse_words()
print(result)
print()
#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))    # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))     # False
print()
#8
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False
print()
#9
import math
def sphere_volume():
    radius = float(input("Radius: "))
    volume = (4/3) * math.pi * radius**3
    print(f"{radius} is {volume:.2f}")
sphere_volume()
print()
#10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
input_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(input_list)
print(input_list)
print(result)
print()
#11
def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]
input_word = input("String: ")
if is_palindrome(input_word):
    print(f"{input_word} - palindrome.")
else:
    print(f"{input_word} - not a palindrome.")
print()
#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
histogram([4, 9, 7])
print()
#13
import random
def guess_the_number():
    print("Hello! What is your name?")
    player_name = input()   
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        player_guess = int(input())
        guesses_taken += 1
        if player_guess < secret_number:
            print("Your guess is too low.")
        elif player_guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_the_number()
