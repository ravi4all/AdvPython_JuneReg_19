class Emp():
    e_id = None
    e_name = None
    e_sal = None
    e_dept = None
    e_list = []

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
obj_2.e_dept = 'IT'
obj_2.e_name = 'Ram'
obj_2.e_sal = 23000
obj_2.e_id = 101
obj_2.showEmp()
