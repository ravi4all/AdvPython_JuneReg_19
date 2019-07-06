import json

def insertUser(username):
    file = open('data_1.json')
    chatData = json.load(file)
    chatData.append({username:[]})
    file.close()
    updateJson(chatData)

def readAllUsers():
    users = []
    file = open('data_1.json')
    chatData = json.load(file)
    # print("JSON Reading")
    for i in range(len(chatData)):
        for key in chatData[i]:
            users.append(key)

    file.close()
    return users

def readChatData(userName = None):
    chat = []
    file = open('data_1.json')
    chatData = json.load(file)
    for data in chatData:
        for key in data.keys():
            if key == userName:
                messages = data[userName]
                chat.append(messages)

    file.close()
    return chat

def insertMessage(userName, msg, rply):
    updatedChat = readChatData(userName)
    if msg['msg'] == '' and rply['rply'] == '':
        print("No Message received")
    elif msg['msg'] == '':
        updatedChat[0].append(rply)
    elif rply['rply'] == '':
        updatedChat[0].append(msg)
    else:
        updatedChat[0].append(msg)
        updatedChat[0].append(rply)

    file = open('data_1.json')
    chatData = json.load(file)
    for i in range(len(chatData)):
        for key in chatData[i].keys():
            if key == userName:
                chatData[i][userName] = updatedChat[0]
                # print(chatData[i])
    # print(chatData)
    file.close()
    return chatData

def updateJson(obj):
    file = open('data_1.json', 'w')
    json.dump(obj, file)
    file.close()

# msg = {'msg':'hello ram how are you ?'}
# rply = {'rply':''}
# insertMessage('Ram',msg,rply)