def hyphenAndSort():

    string1 = input("Enter the String")
    lst =[i for i in string1.split('-')]
    lst.sort()
    print("-".join(lst))

hyphenAndSort()