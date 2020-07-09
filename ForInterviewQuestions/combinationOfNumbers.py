import itertools
def combinations(s):
    comb_arr =[]
    combin_s = itertools.combinations(s,2)
    for char in combin_s:
        str_1 = "".join(char)
        comb_arr.append(str_1)
    print(comb_arr)
    print(len(comb_arr))
combinations("123")