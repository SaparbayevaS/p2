def my_function():
    print("Hello from a function")
my_function()

def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)

#Exercises
def my_function():\
    print("Hello from a function")

def my_function():
    print("Hello from a function")
my_function()

def my_function(fname, lname):
    print(fname)

def my_function(x):
    return x + 5

def my_function(*kids):
    print("The youngest child is " + kids[2])

def my_function(**kid):
    print("His last name is " + kid["lname"])
