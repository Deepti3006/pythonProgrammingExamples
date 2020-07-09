def MissingNumberInArray(arr) :
    i = 0
    total = 1
    n = len(arr)
    sum_expected  =int((n+1)*(n+2)/2)
    print(str(sum_expected))
    sum_actual = sum(arr)
    print(sum_actual)
    print("Number missing " + str(sum_expected-sum_actual))
arr = [1,5,4,3]
MissingNumberInArray(arr)
