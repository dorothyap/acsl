# Dorothy Philip April 16, 2017
# ACSL 2016 - 2017 ACSL Syscraper

import itertools

def count_buildings(heights) :
    count = 0
    max_height = -1
    for height in heights :
        if height > max_height :
            max_height = height
            count = count + 1
    return count

def is_valid(heights, targetleft, targetright) :
    l = count_buildings(heights)
    o = reversed(heights)
    r = count_buildings(o)
    return l == targetleft and r == targetright

def get_count(left, right) :
    s = [1, 2, 3, 4, 5]
    perm_set = itertools.permutations(s)
    cnt = 0;
    for x in perm_set :
        if is_valid(x, left, right) :
            cnt = cnt + 1
    return cnt

results = []
for i in range(5):
    userinput = input()
    data = userinput.split(', ')
    l = int(data[0])
    r = int(data[1])
    x = get_count(l, r)
    results.append(x)

for i in range(5) :
    print (results[i])
