def formNewLine():

    string1 = input("Enter the string")
    count =0
    for i in string1.split(" "):
        count =count+1
        total = count
        if count == 1 and len(i) >1:
            lenf = len(i)
            f_w = i[0]+i[1]
        elif count == total:
            rev_i = i[::-1]
            print(rev_i)
            s_w = rev_i[1]+rev_i[0]
        else:
            f_w = i

    finalStr = f_w+s_w
    print(finalStr)




formNewLine()