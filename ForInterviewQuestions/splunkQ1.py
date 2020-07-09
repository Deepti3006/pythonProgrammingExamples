def fibbonacci(n) :

    if n<0:
        return("Incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibbonacci(n-1) -  fibbonacci(n-2))

for i in range(10):

    print(fibbonacci(i))
