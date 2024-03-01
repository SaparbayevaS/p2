#1
import re
str = input()
x = re.compile(r'a+b*')
if x.fullmatch(str):
    print("yes")
else:
    print("no")
print()
#2
str = input()
x = re.compile(r'a(bb|bbb)')
if x.fullmatch(str):
    print("yes")
else:
    print("no")
print()
#3
str = input()
x = re.compile(r'[a-z]+_[a-z]+')
if x.findall(str):
    print("yes")
else:
    print("no")
print()
#4
str = input()
x = re.compile(r'[A-Z][a-z]+')
if x.findall(str):
    print("yes")
else:
    print("no")
print()
#5
str = input()
x = re.compile(r'a.*b$')
if x.match(str):
    print("yes")
else:
    print("no")
print()
#6
str = input()
x = re.sub(r'[ ,.]', ':', str)
print(x)
print()
#7
snake_case = input()
camel_case = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case)
print(camel_case)
print()
#8
str = input()
x = re.split(r'([A-Z])', str)
print(x)
print()
#9
str = input()
x = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', str)
print(x)
print()
#10
camel_case = input()
snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case).lower()
print(snake_case)
print()
