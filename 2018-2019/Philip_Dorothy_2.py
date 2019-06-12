# Name: Dorothy Philip
# 2018-2019 Contest #2
# Problem : ACSL String Stats
# Language: Python 3.7.2

def letters(userinput) :
    dict = {}
    for i in range(len(userinput)) :
        c = userinput[i]
        if c.isalpha() :
            c = c.upper()
            if c not in dict :
                dict[c] = True
    return  len(dict.keys())

def vowels(userinput) :
    vowels= 0
    for i in userinput:
        if (i=='a' or i=='e' or i=='i' or i=='o'
           or i=='u' or i=='A' or i=='E' or i=='I'
           or i=='O' or i=='U'):
            vowels=vowels+1
    return vowels

def uppercase(userinput) :
    count=0
    for i in userinput:
        if(i.isalpha() and i.isupper()):
            count=count+1
    return count

def frequent(userinput) :
    dict = {}
    for i in range(len(userinput)) :
        c = userinput[i]
        if c.isalpha() :
            c = c.upper()
            if c in dict :
                dict[c] = dict[c] + 1
            else :
                dict[c] = 1
    m = 0 
    for v in dict.values():
        if v > m :
            m = v
    return m                

def longword(userinput) :
    splits = userinput.split();
    longestword = ''
    for i in splits:
        word = ''.join(ch for ch in i if ch.isalpha())
        if len(word) > len(longestword) :
            longestword = word
    return longestword

results = []

userinput= raw_input()

o = letters(userinput)
results.append(str(o))

o = vowels(userinput)
results.append(str(o))

o = uppercase(userinput)
results.append(str(o))

o = frequent(userinput)
results.append(str(o))

o = longword(userinput)
results.append(str(o))

for i in range(5) :
    print(results[i])
