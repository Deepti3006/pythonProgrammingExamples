def ZigZag (arr,n):

    flag = True
    for i in range(n-1):
        if arr[i]> arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        else:
         if  arr[i] <arr[i+1]:
             arr[i],arr[i+1] = arr[i+1],arr[i]

         flag = bool(- flag)
    print(arr)

arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
ZigZag(arr, n)