class Emp():

    def __init__(self,id,name,sal,dept):
        self.e_id = id
        self.e_name = name
        self.e_sal = sal
        self.e_dept = dept
        self.e_list = []

    def showEmp(self):
        self.e_list.append([self.e_id,self.e_name,self.e_sal,self.e_dept])
        print(self.e_list)

    def __del__(self):
        print("Object of",self.e_name,"deleted")

obj_1 = Emp(101,'Ram',24000,'IT')
obj_1.showEmp()

del obj_1

obj_2 = Emp(102,'Shyam',24000,'HR')
obj_2.showEmp()
