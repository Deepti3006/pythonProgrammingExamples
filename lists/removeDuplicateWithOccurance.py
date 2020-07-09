def removeDuplicateWithOccurance():
    arr =[]
    n = int(input("Enter the number of elements"))
    for i in range(n):
        elem = input("Enter the element ")
        arr.append(elem)
    print(arr)
    string1 = input("Enter tehe string you want to remove")
    position = int(input("Enter the position number of String to be removed."))
    count =0
    for y in range(n+1):
        for i in arr:
            if string1 == i:
                if y == position:
                    arr.remove(arr[y])



    print(arr)
removeDuplicateWithOccurance()

