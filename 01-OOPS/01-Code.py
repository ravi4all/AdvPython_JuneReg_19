class Emp():

    e_id = None
    e_name = None
    e_sal = None
    e_dept = None

    def showEmp(self):
        print(self.e_id,self.e_name)

obj_1 = Emp()
obj_1.e_dept = 'IT'
obj_1.e_name = 'Ram'
obj_1.e_sal = 23000
obj_1.e_id = 101
# print(obj_1.__dict__)
obj_1.showEmp()