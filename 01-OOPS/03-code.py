class Emp():

    def __init__(self):
        self.e_id = None
        self.e_name = None
        self.e_sal = None
        self.e_dept = None
        self.e_list = []

    def showEmp(self):
        self.e_list.append([self.e_id,self.e_name,self.e_sal,self.e_dept])
        print(self.e_list)

obj_1 = Emp()
obj_1.e_dept = 'IT'
obj_1.e_name = 'Ram'
obj_1.e_sal = 23000
obj_1.e_id = 101
obj_1.showEmp()

obj_2 = Emp()
obj_2.e_dept = 'HR'
obj_2.e_name = 'Shyam'
obj_2.e_sal = 10000
obj_2.e_id = 102
obj_2.showEmp()
