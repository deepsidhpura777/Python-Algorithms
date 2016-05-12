# -*- coding: utf-8 -*-
"""
Created on Wed May 04 22:30:04 2016

@author: Deep Sidhpura
"""
def checkCollision(board,row,col):
    
    if 1 in board[row]:
        return True

    r = row - 1
    c = col - 1
    while r >= 0 and c >=0 :
        if board[r][c] == 1:
            return True
        r -= 1
        c -= 1
    
    r = row + 1
    c = col - 1
    
    while r < len(board) and c >= 0:
        if board[r][c] == 1:
            return True
        r +=1
        c -=1
        
    return False

def nQueen(board,q,n):
    
    global ctr
    if ctr == n:
        return True
        
    for i in range(n):
        if not checkCollision(board,i,q):
            board[i][q] = 1
            ctr+=1
            if nQueen(board,q+1,n) == True:
                return True
            board[i][q] = 0
            ctr -= 1
    return False
            
            

n = 4
board = []
ctr = 0
for i in range(n):
    board.append([0]*n)
    
nQueen(board,0,n)

print board