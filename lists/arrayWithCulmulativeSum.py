def arrayWithCulmulativeSum():
    n = int(input("Enter the number of Elements"))
    a_c=[]
    a =[]
    for i in range(0,n):
        elem = int(input("Enter the element"))
        a.append(elem)
    print(a)
    for i in range(0,len(a)):
        elem = sum(a[0:i+1])
        print(elem)
        a_c.append(elem)
    print(a_c)
arrayWithCulmulativeSum()