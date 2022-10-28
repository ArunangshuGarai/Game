import random




win_set=[]
grid=[]
pos_set=[]

for i in range(4):
    grid.append([0,0,0,0])



while(not(len(pos_set)==5)):
    
    posx=random.randint(0,3)#0 1 2 3
    posy=random.randint(0,3)
    # print(posx,posy)
    if(not([posx,posy] in pos_set)):
        pos_set.append([posx,posy])
        # grid[posx][posy]=win_set[i]
a,b=[],[]
rand=0
while(not(len(win_set)==5)):
    rand=random.randint(1,99)
    if(rand not in win_set):
        win_set.append(rand)
        a,b=pos_set[len(win_set)-1][0],pos_set[len(win_set)-1][1]
        grid[a][b]=win_set[len(win_set)-1]


for i in range(4):
    for j in range(4):
        n=random.randint(1,99)
        if grid[i][j]==0 :
            # print(n in grid[i][j])
            while(n in grid[0] or n in grid[1] or n in grid[2] or n in grid[3]):
                n=random.randint(1,99)
            else:            
                grid[i][j]=n

#[
# [0,0,0,0], posx=2, posy=3
# [0,0,21,0],
# [0,0,0,0],
# [0,0,0,0]]
    
print(win_set)
print(pos_set)
print(grid)

    

# print(main()[0])