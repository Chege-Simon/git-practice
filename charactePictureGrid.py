grid = [['.','.','.','.','.','.'],
        ['.','O','O','.','.','.'],
        ['O','O','O','O','.','.'],
        ['O','O','O','O','O','.'],
        ['.','O','O','O','O','O'],
        ['O','O','O','O','.','.'],
        ['O','O','O','O','.','.'],
        ['.','O','O','.','.','.'],
        ['.','.','.','.','.','.']]




    
for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print('')

mystr1 = ''
for x in range(len(grid)):
    
    mystr1 += str(grid[x][0])
    
    
    mystr2 = '\n'
for x in range(len(grid)):    
    
    mystr2 += str(grid[x][1])
    
    
    mystr3 = '\n'
for x in range(len(grid)):    
    
    mystr3 += str(grid[x][2])
    

    mystr4 = '\n'
for x in range(len(grid)):    
    
    mystr4 += str(grid[x][3])
    

    mystr5 = '\n'
for x in range(len(grid)):    
    
    mystr5 += str(grid[x][4])
    
    mystr6 = '\n'
for x in range(len(grid)):    
    
    mystr6 += str(grid[x][5])
    
print(mystr1 + mystr2 + mystr3 + mystr4 + mystr5 + mystr6 + mystr6) 
