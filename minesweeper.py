#minesweeper game using classes
from random import randint

class tile:
        def __init__(self,x,y):
                self.x = x
                self.y = y
                self.openStatus = 0
                self.hasBomb = False
                self.nearbyBombs = 0
                self.flag = False
                self.qmark = False

        
        def nearbyBomb(self,grid):
                counter = 0 
                for j in {(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)}:
                        try:
                                if grid[(self.x + j[0], self.y + j[1])].hasBomb:
                                        counter+=1
                        except KeyError:
                                continue
                self.nearbyBombs = counter

        
        
def placeBombs(grid):
        totalBombs = randint(10,15)
        bombsPlaced = 0
        
        while bombsPlaced <= totalBombs:
                
                i = randint(0,7)
                j = randint(0,7)
                grid[(i,j)].hasBomb = True
                bombsPlaced+=1
                                
def openTile(grid,x,y):

        
                if grid[(x,y)].nearbyBombs == 0:
                        grid[x,y].openStatus = True
                        
                        for i in {(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)}:
                                try:
                                        if grid[(x+i[0],y+i[1])].nearbyBombs == 0 and grid[(x+i[0],y+i[1])].openStatus == False :
                                                openTile(grid,x+i[0],y+i[1])
                                        #print(i)
                                        grid[(x+i[0],y+i[1])].openStatus = True
                                except KeyError:
                                        continue
                        return       
                else:
                        grid[x,y].openStatus = True
                        return

                 
        
def updateGrid(grid,choice,x,y):
        

                if grid[(x,y)].hasBomb: 
                        print('Game Over!')
                        printGrid(grid,1)
                        exit()
                else:
                        match choice:
                                case '1' : openTile(grid,x,y)   #open tile                                      
                                case '2' : grid[(x,y)].flag = True             #flag tile
                                case '3' : grid[(x,y)].qmark = True            #question mark tile


##def printGridcopy(grid):
##        
##                for i in range(0,8):
##                        print('|',end=' ')
##                        for j in range(0,8):
##                                if grid[(i,j)].hasBomb:
##                                        print('*|',end='')
##                                
##                                else:
##                                        
##                                        print(grid[(i,j)].nearbyBombs,end='| ')
##              
##                                
##                        print('\n_________________________')
                                
def printGrid(grid,gameOver=0):
        
        if gameOver:
                for i in range(0,8):
                        print('| ',end='')
                        for j in range(0,8):
                                if grid[(i,j)].hasBomb:
                                        print(end='*| ')
                                
                                else:
                                        print(grid[(i,j)].nearbyBombs,end='| ')
                                
                        print('\n_________________________')


        else:
                for i in range(0,8):
                        print('| ',end='')
                        for j in range(0,8):
                                
                                if grid[(i,j)].openStatus:
                                        print(grid[(i,j)].nearbyBombs,end='| ')
                                        
                                elif grid[(i,j)].flag:
                                        print(end='F| ')
                                        
                                elif grid[(i,j)].qmark:
                                        print(end='?| ')
                                else:
                                        print(' |',end=' ')
                                        
                        print('\n_________________________')
                
                                
if __name__ == "__main__":
                
        grid = {}
        for i in range(0,8):
                for j in range(0,8):
                        grid[(i,j)] = tile(i,j)
        placeBombs(grid)
        
        for Tile in grid:
                grid[Tile].nearbyBomb(grid)

        #printGridcopy(grid)                
        while True:
                tilex = int(input("Enter x coordinate of tile: "))
                tiley = int(input("Enter y coordinate of tile: "))

                print("Press 1 to open tile")
                print("Press 2 to flag tile")
                print("Press 3 to question mark tile")
                choice = input("Enter your choice: ")
                updateGrid(grid,choice,tilex,tiley)
                printGrid(grid)
        
