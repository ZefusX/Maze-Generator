import numpy as np
import random
import time
from matplotlib import pyplot as plt

class Maze:
    def __init__(self, size) -> None:
        self.grid = np.ones((size,size))
        self.size = size
        
    def get_grid(self):
        return self.grid
        
    def get_neighbours(self,x,y):
        n=[]
        if x+2 < self.size-2:
            n.append((x+2,y))
        if x-2 > 0:
            n.append((x+2,y)) 
        if y+2 < self.size-2:
            n.append((x,y+2))
        if y-2 > 0:
            n.append((x,y-2))
        return n
    
    def get_closest_cell(self,x,y):
        closest_c = []
        if x+2 < self.size-2:
            if self.grid[x+2][y] == 1:
                closest_c.append((x+2,y))
        if x-2 > 0:
            if self.grid[x-2][y] == 1:
                closest_c.append((x-2,y))
        if y+2 < self.size-2:
            if self.grid[x][y+2] == 1:
                closest_c.append((x,y+2))
        if y-2 > 0:
            if self.grid[x][y-2] == 1:
                closest_c.append((x,y-2))
        return closest_c
    
    def generator(self):
        for i in range(len(self.grid)):
            self.grid[0][i]=0
        
        for y in range(0,self.size,2):
            run = []
            for x in range(0,self.size,2):
                self.grid[x][y]=0
                
                run.append((x,y))
                r=random.randint(0,1)
                if r >= 1 and y<self.size-2:
                    self.grid[x][y+1]=0
                elif r == 0 and x<self.size-2:
                    n=random.choice(run)
                    self.grid[n[0]-1][n[1]]=0
                    run = []
    
    def display_maze(self):
        self.display_grid = []
        for row in self.grid:
            for col in row:
                if col == 1:
                    self.display_grid.append([255,0,0])
                else:
                    self.display_grid.append([0,0,255])
        plt.imshow(self.grid, interpolation='nearest')
        plt.show() 

    
        
    
        
maze = Maze(97)
maze.generator()
print(maze.get_grid())
maze.display_maze()
 
        