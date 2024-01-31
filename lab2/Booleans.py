#Examples
print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))
print(bool(15))
print(bool("abc"))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))

#Exercises
print(10 > 9)
#True
print(10 == 9)
#False
print(10 < 9)
#False
print(bool("abc"))
#True
print(bool(0))
#False