def fibbonacciSeries():

    n =int(input("Enter the elements in serves"))
    a = []
    first =0
    second =1
    a.append(first)
    a.append(second)
    for i in range(2,n):
        next = second-first
        a.append(next)
        print(a)
        first=second
        second=next


fibbonacciSeries()


