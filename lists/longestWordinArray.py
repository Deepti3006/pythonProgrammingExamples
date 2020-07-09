def longestWordInArray():

    n = int(input("total number of ele"))
    a=[]

    for i in range(n):
        elem = input("Enter total number of element")
        a.append(elem)
    len_a_0 = len(a[0])
    print(str(len_a_0))
    for string1 in a:
        if len(string1) > len_a_0:
            print(string1)
longestWordInArray()




