def factorialWithRecursion(n):

        if n == 1:
            return 1
        if n==0:
            return 0
        else:
            return n*factorialWithRecursion(n-1)
print(factorialWithRecursion(5))