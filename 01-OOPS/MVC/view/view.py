import sys
sys.path.append('..')
from controller import controller

def register():
    id = input("Enter id : ")
    name = input("Enter name : ")
    course = input("Enter course : ")
    data = controller.registerStudent(id,name,course)
    # print("Welcome",name)
    print(data)

def login():
    id = input("Enter ID : ")
    name = input("Enter Name : ")
    data = controller.loginStudent(id,name)
    # print(data)

while True:
    print("""
    1. Register
    2. Login
    """)

    ch = input("Enter your choice : ")
    operations = {"1":register,"2":login}
    operations.get(ch)()