def commaCode(userList):
    commaCodedText = ''
    for i in range(len(userList)):
        if (i == len(userList) - 1):
            commaCodedText += 'and ' + userList[-1]
            break
        commaCodedText += (userList[i] + ', ')    
    return commaCodedText
spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))
cheese = []
print(commaCode(cheese))