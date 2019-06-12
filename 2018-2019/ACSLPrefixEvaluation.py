# Name: Dorothy Philip
# 2018-2019 Contest #3
# Problem : Prefix Evaluation
# Language: Python 3.7.2

def evaluate(expr):
    y = expr.split()
    length = len(y)
    stack=[]
    i = length-1
    while i >= 0 :
        s = y[i]
        i = i-1
        if s.isdigit() :
            stack.append(s)
        else :
            a = stack.pop()
            b = stack.pop()
            if s == '+' :
                o = int(a)+ int(b)
                stack.append(str(o))
            elif s == '-' :
                o = int(a) - int(b)
                stack.append(str(o))
            elif s == '*' :
                o = int(a) * int(b)
                stack.append(str(o))
            elif s == '@' :
                c = stack.pop()
                if int(a) >= 0 :
                    o = int(b)
                else:
                    o = int(c)
                stack.append(str(o))
    return(stack.pop())
    
results = []
userinput = input()
o = evaluate(userinput)
results.append(str(o))

userinput = input()
o = evaluate(userinput)
results.append(str(o))

userinput = input()
o = evaluate(userinput)
results.append(str(o))

userinput = input()
o = evaluate(userinput)
results.append(str(o))

userinput = input()
o = evaluate(userinput)
results.append(str(o))

for i in range(5) :
        print(results[i])



