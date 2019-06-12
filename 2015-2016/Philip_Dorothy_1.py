# Name: Dorothy Philip
# 2015-2016 Contest #1
# Problem : ACSL CHMOD JUNIOR DIVISION
# Language: Python 2.7.6

def CHMOD(rwx):
    if rwx == "000":
        return '---'
    if rwx == "001":
        return '--x'
    if rwx == "010":
        return '-w-'
    if rwx == "011":
        return '-wx'
    if rwx == "100":
        return 'r--'
    if rwx == "101":
        return 'r-x'
    if rwx == "110":
        return 'rw-'
    if rwx == "111":
        return 'rwx'
    
      
def octalcode(octal) :
    if octal == 0:
        return '000'
    if octal == 1:
        return '001'
    if octal == 2:
        return '010'
    if octal == 3:
        return '011'
    if octal == 4:
        return '100'
    if octal == 5:
        return '101'
    if octal == 6:
        return '110'
    if octal == 7:
        return '111'


num1 = []
num2 = []
num3 = []
for i in range (0,5):
    x = raw_input()
    n = x.split(", ")
    r1 = int(n[0])
    r2 = int(n[1])
    r3 = int(n[2])
    num1.append(r1)
    num2.append(r2)
    num3.append(r3)

for i in range (0,5):
    x = num1[i]
    x1 = num2[i]
    x2 = num3[i]
    y = octalcode(x)
    y1 = octalcode(x1)
    y2 = octalcode(x2)
    print octalcode(x) + ' ' + octalcode(x1) + ' ' + octalcode(x2), " and ", CHMOD(y) + ' ' + CHMOD(y1) + ' ' + CHMOD(y2)
 

    

    
















   
