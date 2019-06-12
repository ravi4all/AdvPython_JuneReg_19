'''
num = int(input("Enter a number : "))
flag = True
for i in range(2,num):
    if num % i == 0:
        # print("Not Prime")
        flag = True
        break
    else:
        # print("Prime Number")
        flag = False

if flag:
    print("Not Prime")
else:
    print("Prime")
'''

num = int(input("Enter a number : "))
flag = True
for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")