# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:23:34 2019

@author: OCEAN
"""

def magic_Square(n):
    magic_square=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magic_square.append(l)    
    
    i=n//2
    j=n-1  #this is the condition for 1
    num=n*n
    count=1
    while(count<=num):
        if (i<0 and j==n):
            i=0
            j=n-2
        else:
            if i<0:
                i=n-1
            if j==n:
                j=0
        if(magic_square[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magic_square[i][j]=count
            count+=1
        i=i-1
        j=j+1
    print("the value of row or column and diaginal is"+str(n*(n**2+1)/2))
    for i in range(n):
        for j in range(n):
            print(magic_square[i][j],end=" ")
        print()   
magic_Square(3)        