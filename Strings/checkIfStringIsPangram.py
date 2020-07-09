from string import ascii_lowercase as asc_lower
def checkIfStringIsPangram():

    string1 = input("Input the strring to be checked")
    ss_str = set(string1.lower())
    if (set(asc_lower) -ss_str == set([])):

        print("The sentende ic pangram")
    else:
        print("Sentence is not pangram")
checkIfStringIsPangram()