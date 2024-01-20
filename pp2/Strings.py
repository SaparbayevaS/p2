x = "Hello World"
print(len(x))

txt = "Hello World"
y = txt[0]
z = txt[2:5]
print(y, z)

txt = " Hello World "
txt = txt.strip()
print(txt)
print(txt.upper(), " ", txt.lower())
print(txt.replace("H", "J"))

age = 17
txt = "Hello, my name is Sabina and I am {}"
print(txt.format(age))