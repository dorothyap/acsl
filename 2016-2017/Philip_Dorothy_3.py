#Name: Dorothy Philip
#2016-2017 Contest #3
#Problem: Lights Out ACSL Junior Division
#Language: Python 3.6.0

#!/usr/bin/env python
offsets = [[0, 0],
           [-1, 0],[1, 0],[0, 1],[0, -1],
           [-2, 0],[2, 0],[0, -2],[0, 2],
           [1, -1],[1, 1],[-1, -1],[-1, 1]]

def places(r, c) :
    results = []
    for o in offsets:
           ox = o[0]
           oy = o[1]
           x = r + ox
           y = c + oy
           if (x > 0 and x <=8 and y > 0 and y <=8) :
               results.append([x, y])
    return results

results = []
                  
for i in range(5) :
    userinput = input()
    data = userinput.split(', ')
    nrows = int(data[0])
    Matrix = [[False for x in range(8)] for y in range(8)]
    for i in range(1, nrows+1) :
        d = data[i]
        ncols = len(d)
        r = int(d[0])
        for j in range(1, ncols) :
            c = int(d[j])
            Matrix[r-1][c-1] = True
    t = data[nrows + 1]
    r = int(t[0])
    c = int(t[1])
    tiles = places(r, c)
    for m in tiles:
           x = m[0]-1
           y = m[1]-1
           Matrix[x][y] = not Matrix[x][y]

    cnts = 0
    for r in range(8):
           for c in range(8):
               if Matrix[r][c]:
                   cnts = cnts + 1
    results.append(cnts)
        
for i in range(5) :
    print (results[i])
