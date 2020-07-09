def unionOfTwoLists():
    arr_a =[]
    arr_b=[]
    n1 = int(input("Enter the total number of elements in Arr_A"))
    n2 = int(input("Enter the total number of elements in Arr_B"))
    for i in range(n1):
        elem1 = int(input("Enter the element in arr_A"))
        arr_a.append(elem1)
    for i in range(n2):
        elem2 = int(input("Enter the element in arr_B"))
        arr_b.append(elem2)

    print(arr_b)
    print(arr_a)

    arr_union = list(set().union(arr_a,arr_b))
    print(arr_union)

    arr_intersection = list(set().intersection(arr_a,arr_b))
    print(arr_intersection)
unionOfTwoLists()


