def getNumbersInFile():
    count =0
    with open("1.txt","r+") as f:
        for line in f:
            words = line.split(" ")
            for word in words:
                for letter in word:
                    if letter.isdigit():
                        count =count+1
                    print("{} , {}".format(letter ,count))
getNumbersInFile()

