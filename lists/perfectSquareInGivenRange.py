import math

def findNumberWhichArePerfectSquare():

    n = int(input("Enter the range of Numbers which need to be checked"))
    p_s =[]
    s_m =[]

    for i in range(1,n):
        root = math.sqrt(i)
        if int(root + 0.5) ** 2 == i and sum(list(map(int, str(i)))) <10:
            print("Perfect Square")
            p_s.append(i)
    print(p_s)

def findIfNumberIsPErfectSquare():

    n = int(input("Enter the number"))
    root = math.sqrt(n)
    if int(root+0.5) ** 2 == n:
        print("Perfect Square")
findIfNumberIsPErfectSquare()



