def readSentencePrintLargestWord():
    s = input("Input the sentence")
    count =0
    words=[]
    for word in s.split(" "):
        print(word)
        words.append(word)
        count = count+  1
    print(count)
    for i in range(1,len(words)):
        max_size = len(words[0])
        if len(words[i]) > max_size:
            max_size = len(words[i])
            word_max= words[i]
        elif len(words[i]) == max_size:
            max_size == len(words[0])
    print("{},{}" .format(word_max ,max_size))


readSentencePrintLargestWord()