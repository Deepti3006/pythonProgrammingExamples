def removeDuplicateNumbersInList():

    a=[1,5,7,8,2,5,1]
    unique =[]
    for i in range(len(a)):
        if a[i] not in unique:
            unique.append(a[i])
    print(unique)
removeDuplicateNumbersInList()