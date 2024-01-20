carname = "Volvo"
x = 50
y = 10
print(x + y)

z = x + y
print(z)

a, b, c = "Orange", "Banana", "Cherry"
print(a, b, c)

a = b = c = "Orange"
print(a, b, c)

def myfunc():
    global x
    x = "fantactic"
    print(x)
myfunc()