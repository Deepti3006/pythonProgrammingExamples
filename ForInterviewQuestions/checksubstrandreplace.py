def checkSubstrAndCheck():
    s1 = input("Enter complete String")
    s2 = input("Enter substr")

    index = s1.find(s2)
    if index == -1:
        print(":)")
    else:
        s3 = s2[::-1]
        s1 = s1.replace(s2,s3)
        print(s1)
checkSubstrAndCheck()