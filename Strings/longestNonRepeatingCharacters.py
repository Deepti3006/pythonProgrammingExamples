def longestNonRepeatignStringInWord() :

    s = input("Enter the string  : ")

    for i in range(len(s)):
        seen = []
        longest = 0
        for j in s[i:]:
            if j in seen:
                break
            else:
                seen.append(j)
        longest = max(len(seen), longest)
        print(longest)
        return longest
longestNonRepeatignStringInWord()