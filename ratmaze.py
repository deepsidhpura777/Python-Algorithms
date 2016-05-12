# -*- coding: utf-8 -*-
"""
Created on Thu May 05 16:24:32 2016

@author: Deep Sidhpura
"""

def ratmaze(maze,solution,row,col):
    
    if row == len(maze)-1 and col == len(maze)-1:
        solution[row][col] = 1
        return True
    if row >=0 and row < len(maze) and col >=0 and col < len(maze) and maze[row][col] == 1:
        solution[row][col] = 1
        if ratmaze(maze,solution,row+1,col) == True:
            return True
        if ratmaze(maze,solution,row,col+1) == True:
            return True
        solution[row][col] = 0
        return False
    return False

maze = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
solution = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ratmaze(maze,solution,0,0)
print solution