def swapFirstAndLast():
    a=[1,3,5,8,22,44,60]
    f_elem = a[0]
    print(f_elem)
    l_elem= a[-1]
    print(l_elem)
    temp = a[0]
    a[0] =a[-1]
    print(f_elem)
    a[-1] =temp
    print(l_elem)

    print(a)

swapFirstAndLast()