# Name: Dorothy Philip
# 2015-2016 Contest #2
# Problem : ACSL STRINGS JUNIOR DIVISION
# Language: Python 2.7.6

def substr(s , start , length) :
    i1 = index1(s, start)
    i2 = index2(s, start, length)
    return s[i1: i2]

def index1(s, start):
    l = len(s)
    if start >= 0 :
        return start
    else :
        return l + (start)

def index2(s, start, length):
    l = len(s)
    if length == 0 :
        return l 
    elif length > 0 :
        return start + length 
    else :
        return l + (length)

i1 = []
i2 = []
s = raw_input().strip()
for i in range(0,5):
    x = raw_input()
    n = x.split(', ')
    i1.append(n[0].strip())
    i2.append(n[1].strip())
   
for i in range (0,5):
    x = int(i1[i])
    x1 = int(i2[i])
    print substr(s, x, x1)
    
        
        
