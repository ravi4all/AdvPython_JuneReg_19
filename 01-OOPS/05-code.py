class Student():

    def __init__(self,id,name,grade,hobby):
        self.id = id
        self.name = name
        self.grade = grade
        self.__hobby = hobby # private variables

    def showDetails(self):
        print(self.id,self.name,self.grade,self.__hobby)

obj = Student(101,'Ram','A','Cricket')
obj.showDetails()
print(obj)