def sortWithSecindSublist(a):
    for i in range(len(a)):
        for j in range(len(a) -1):
            if a[j][1] > a[j+1][1]:
                a[j],a[j+1] = a[j+1],a[j]
    print(a)
a=[['A',34],['B',21],['C',26]]
sortWithSecindSublist(a)