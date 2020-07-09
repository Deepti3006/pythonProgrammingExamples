import random

def randomNumberArray():
    arr = []
    for i in range(1,21):
        elem = random.randint(1,20)
        arr.append(elem)
    print(arr)
    print(str(len(arr)))
randomNumberArray()
