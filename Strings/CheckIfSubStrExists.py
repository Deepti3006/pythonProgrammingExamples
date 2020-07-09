def checkForSubstring():

    string1 = input("Enter the string")
    find_sub =input("Enter the substring")
    if(string1.find(find_sub) == -1):
        print("I am not having sub str")
    else:
        print("I am sub str")
checkForSubstring()