# Name: Dorothy Philip
# 2018-2019 Contest #1
# Problem : ACSL Digit Reassembly Junior Division
# Language: Python 2.7.11

def NumberofDigits() :
    userinput = raw_input()
    return(len(userinput))

def SumofDigits() :
    input_string = raw_input()
    mylist  = list(input_string)
    sum = 0
    for num in mylist:
        sum += int(num)
    return(sum)

def SumofOddLocations() :
    userinput = raw_input()
    lst = list(userinput)
    i = 0
    sum = 0
    while (i < len(lst)) :
        sum = sum + int(lst[i])
        i = i + 2
    return sum

def HowManyFours() :
    userinput = raw_input()
    mylist  = list(userinput)
    count = 0
    for i in range(len(mylist)) :
        if mylist[i] == '4' :
            count = count + 1
    return count

def Median():
    userinput = raw_input()
    mylist  = list(userinput)
    return mylist[(len(mylist)/2-1)]

results = []

o = NumberofDigits()
results.append(str(o))

o = SumofDigits()
results.append(str(o))

o = SumofOddLocations()
results.append(str(o))

o = HowManyFours()
results.append(str(o))
                  
o = Median()
results.append(str(o))

for i in range(5) :
    print results[i]

