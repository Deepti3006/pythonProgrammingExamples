def firstAsNumberSecondAsTuple():
    n = int(input("Enter the total number of elements in the tuple"))
    a=[]
    for i in range(1,n):
        if i%2 == 0:
            elem = i*i
            a.append(elem)
        else:
            elem = i
            a.append(elem)
        print(a)
firstAsNumberSecondAsTuple()