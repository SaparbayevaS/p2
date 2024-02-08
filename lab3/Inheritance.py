class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname):
       super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()




#Exercise

class Person:
    def __init__(self, fname):
        self.firstname = fname
    def printname(self):
        print(self.firstname)
class Student(Person):
    pass
x = Student("Mike")
x.printname()
