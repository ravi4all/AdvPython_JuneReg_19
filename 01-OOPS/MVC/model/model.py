import pickle
import csv

class Student():

    def __init__(self,id,name,course):
        self.__id = id
        self.__name = name
        self.__course = course

    def __str__(self):
        return self.__id + "," + self.__name + "," + self.__course

# students = []
def register(id,name,course):
    s = Student(id,name,course)
    # students.append(s)
    # file = open('users.pkl','ab')
    # pickle.dump(s,file)
    # file.close()
    with open('users.csv','a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id,name,course])
    return s

# def login(id,name):
    # for i in range(len(students)):
    #     x = str(students[i]).split(",")
    #     print(x,x[0],x[1])
    #     if x[0] == id and x[1] == name:
    #         return x
    # else:
    #     return "User Not Found"
    # file = open('users.pkl','rb')
    # data = pickle.load(file)
    # print(data)
    # file.close()

# Unique ID