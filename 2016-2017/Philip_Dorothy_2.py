# Name: Dorothy Philip
# 2016-2017 Contest #2
# Problem: ACSL Ascending JUNIOR DIVISON
# Language: Python 2.7.11

def process(s) :
        r = []
        i = 0
        j = 1
        PC = -1
        y = len(s)
        while (j <= y) :
                candidate = int(s[i:j])
                if candidate > PC :
                        PC = candidate
                        i = j
                        j = i+1
                        r.append(candidate)
                else:
                        j = j + 1
        return r

results = []
for n in range(5):
        userinput = raw_input()
        v = process(userinput)
        results.append(v)
        
for n in results :
        for x in n :
                print str(x) + ' ',
        print
		
	
