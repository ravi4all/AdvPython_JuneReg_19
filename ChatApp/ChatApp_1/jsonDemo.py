import json

file = open('data.json')

users = []
data = json.load(file)
for i in range(len(data)):
    for key in data[i]:
        print(key)
        users.append(key)
# users.append([data[0].keys()[0],data[1].keys()])
print(users)
file.close()