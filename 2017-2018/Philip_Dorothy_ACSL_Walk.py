# Name: Dorothy Philip
# 2017-2018 Contest #3
# Problem : ACSL Walk Junior Division
# Language: Python 2.7.11

def create_grid(): ### Creates s 4x4 grid
    grid = [[] for i in range(4)]
    for i in range(4):
        grid[i] = [0 for j in range(4)]
    return grid

    
def assign_grid(grid, data) : ###assigns grid values (row, column)
    r = 0 ## row number 
    for d in data:
        x = d.strip()  ### Remove whitespace
        y = list(x)    ### Convert to list
        skipcnt = 4 - len(y) ### Check how many zeros to add in the front
        j = 0
        for elem in y :
            c = j + skipcnt ; ###column number
            grid[r][c] = int(elem) ### assigning to column
            j = j + 1        
        r = r + 1  ### go for the next row

def move(grid, r,  c) : ### make a move on the position
    m = grid[r][c] ## move value
    grid[r][c] = (m + 1) % 4  ## change the next move value for current position
    if m == 0 : ### if the value is 0 move right 
        c = c + 1
    elif m == 1 : ### if the value is 1 move left 
        c = c - 1
    elif m == 2 : ### if the value is 2 move up 
        r = r - 1
    elif m == 3 : ### if the value is 3 move down 
        r = r + 1
    r = r % 4 ### checks to see whether there is a remainder and if so it loops back row
    c = c % 4 ### checks to see whether there is a remainder and if so it loops back column
    return (r, c)    

user_input = raw_input()
data = user_input.split(', ') ### read the initial values for the grid

results = [] 
for i in range(5) : ### takes in 5 user inputs and processes it 
    grid = create_grid()  ### create grid
    assign_grid(grid, data)  ### assign the initial values
    userinput = raw_input()  ### read the position row, column  
    position = userinput.split(', ') ### splits output 
    r = int(position[0])    
    c = int(position[1]) 
    p = ''
    r = r - 1 ### python row
    c = c - 1 ### python column
    for k in range(6) : ### applies the move 6 times 
        v = move(grid, r, c) ### moves the grid each time the row and column changes 
        r = v[0] ### new row position 
        c = v[1] ### new column position
    p = str(r+1) + ', ' + str(c+1) ### final position for the current vaue
    results.append(p) ### add it to result

for i in range(5) :  ### print all the results
    print results[i]
    
