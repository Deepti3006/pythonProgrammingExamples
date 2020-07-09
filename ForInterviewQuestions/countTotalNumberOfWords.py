import re
def countTotalNumberOfWords():

    arr =[]
    arr_special =[]
    arr_alp = []
    with open("1.txt", "r+") as f:
        for line in f:
            words = line.split()
            regx = re.compile('[$&]')
            for word in words:
                if word.isalnum():
                    arr_alp.append(word)
                elif regx.search(word):
                    arr_special.append(word)
                else:
                    arr.append(word)
        print(len(arr))
        print(len(arr_alp))
        print(len(arr_special))
countTotalNumberOfWords()