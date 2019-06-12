# Name: Dorothy Philip
# 2015-2016 Contest #4
# Problem : ACSL RegExp JUNIOR DIVISION
# Language: Python 2.7.6

import re
userinput = raw_input()
y = userinput.split(', ')
y1 = []
for r in y:
    if r.strip() == '#' :
        y1.append('')
    else:
        y1.append(r.strip())

results = []

for i in range(5):
    rexp = raw_input()
    data = '^' + rexp + '$'
    r = re.compile(data)
    a = []
    for s in y1:
        if r.match(s):
            a.append(s)
    if len(a) == 0:
        v = 'NONE'
    else :
        y2 = []
        for j in a:
            if j == '' :
                y2.append('#')
            else:
                y2.append(j)
        v = ', '.join(y2)
    results.append(v)

for r in results:
    print r
        


    
    
