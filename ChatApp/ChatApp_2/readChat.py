import json

def isUserExist(username):
    file = open('data.json')
    userExist = False
    user = True
    chatData = json.load(file)
    if len(chatData) == 0:
        chatData.append({username : []})

    else:
        while user:
            for i in range(len(chatData)):
                for key in chatData[i]:
                    if key == username:
                        print("User Exist")
                        userExist = True
                        user = False
                    else:
                        userExist = False
            user = False

    if userExist == False:
        print("User do not exist")
        chatData.append({username : []})

    file.close()
    updateJson(chatData)

def readAllUsers():
    users = []
    file = open('data.json')
    chatData = json.load(file)
    for i in range(len(chatData)):
        for key in chatData[i]:
            users.append(key)

    file.close()
    return users

def readChatData(userName = None):
    chat = []
    file = open('data.json')
    chatData = json.load(file)
    for data in chatData:
        for key in data.keys():
            if key == userName:
                messages = data[userName]
                chat.append(messages)

    file.close()
    return chat

def insertMessage(userName, msg, rply):
    # userName = 'Amit'
    # msg = {'msg':'hi'}
    # rply = {'rply':'hmmmmm'}
    isUserExist(userName)
    updatedChat = readChatData(userName)
    if len(updatedChat) == 0:
        updatedChat.append(msg)
        updatedChat.append(rply)
    else:
        if msg['msg'] == '' and rply['rply'] == '':
            print("No Message received")
        elif msg['msg'] == '':
            updatedChat[0].append(rply)
        elif rply['rply'] == '':
            updatedChat[0].append(msg)
        else:
            updatedChat[0].append(msg)
            updatedChat[0].append(rply)

    file = open('data.json')
    chatData = json.load(file)
    for i in range(len(chatData)):
        for key in chatData[i].keys():
            if key == userName:
                chatData[i][userName] = updatedChat[0]
                break
                # print(chatData[i])
    # print(chatData)
    file.close()
    # return chatData
    updateJson(chatData)

def updateJson(obj):
    file = open('data.json', 'w')
    json.dump(obj, file)
    file.close()

# readAllUsers()
# readChatData('Ram')
# insertMessage()
# isUserExist()