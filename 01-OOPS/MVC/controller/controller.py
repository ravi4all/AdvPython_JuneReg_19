import sys
sys.path.append('..')
from model import model

def registerStudent(id,name,course):
    data = model.register(id,name,course)
    return data

def loginStudent(id,name):
    data = model.login(id,name)
    return data