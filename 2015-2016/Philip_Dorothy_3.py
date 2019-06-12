# Name: Dorothy Philip
# 2015-2016 Contest #3
# Problem : ACSL ABC JUNIOR DIVISION
# Language: Python 2.7.6

class Board(object):
    
    def __init__(self):
        self._grid = ['E' for i in range(10)]

    def SetGrid(self, i, c) :
        self._grid[i] = c

    def Valid(self, x) :
        options = [[], [2,3,4,7], [1,3,5,8], [1,2,6,9], [1,7,5,6], [2,8,4,6], [3,9,4,5], [1,4,8,9], [2,5,7,9],[7,8,3,6]]
        for i in range(1,10) :
            if self.InvalidPlace(x, options[i], x[i]) :
                return False
        return True                        
            
    def InvalidPlace(self, b, moves, c) :
        for i in moves :
            if b[i] == c :
                return True
        return False

    def Play(self):
        options = [[]]
        for i in range(1,10) :
            if self._grid[i] != 'E' :
                options.append([self._grid[i]])
            else :
                options.append(['A', 'B', 'C'])

        for i1 in options[1] :
            for i2 in options[2] :
                for i3 in options[3] :
                    for i4 in options[4] :
                        for i5 in options[5] :
                            for i6 in options[6] :
                                for i7 in options[7] :
                                    for i8 in options[8] :
                                        for i9 in options[9] :
                                            x = ['E', i1, i2, i3, i4, i5, i6, i7, i8, i9]
                                            if self.Valid(x) :
                                                return x
        return 'Error'
                                

results = []
for i in range(5):
    b = Board()
    user_input = raw_input()
    data = user_input.split(', ')
    n = int(data[0].strip())
    for i in range(n):
        loc =int(data[i * 2 + 1].strip())
        C = data[i * 2 + 2].strip()
        b.SetGrid(loc, C)
    x = b.Play()
    results.append(''.join(x[1:]))
    
for b in results:
    print b
    
        
                                       
