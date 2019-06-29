class Person():
    def __init__(self,name,age,address,sal):
        self.name = name
        self.age = age
        self.address = address
        self.sal = sal
        self.company = 'TCS'
        self.branch = 'Noida'

    def showDetails(self):
        print("Parent Class Call")
        print("Welcome to {}".format(self.company))
        print("Your branch is {}".format(self.branch))

class Emp(Person):
    def __init__(self,name,age,address,sal):
        super().__init__(name,age,address,sal)

    def showPerson(self):
        print("Name : {}".format(self.name))
        print("Age : {}".format(self.age))
        print("Address : {}".format(self.address))
        print("Salary : {}".format(self.sal))

    def showDetails(self):
        print("Child Class Call")
        print("Welcome to {}".format(self.company))
        print("Your branch is {}".format(self.branch))

emp = Emp('Ram',30,'Delhi',45000)
emp.showDetails()
emp.showPerson()
