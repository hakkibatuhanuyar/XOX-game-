# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:10:45 2019

@author: Batuhan
"""
import random
import sys    

def play():
    d=""
    xox=[[d,d,d], 
         [d,d,d],
         [d,d,d]]   
    empty_points=[[0,0],[0,1],[0,2],
                  [1,0],[1,1],[1,2],
                  [2,0],[2,1],[2,2]]
    while True:
        
        solution1={"x","x","x"}
        solution2={"o","o","o"}   

        x=int(input("satır giriniz : "))-1

        if int(x)>2:
            print("---0,1,2 koordinatları girebilirsiniz---")
            sys.exit()

        y=int(input("sütun giriniz : "))-1

        if int(y)>2:
            print("---0,1,2 koordinatları girebilirsiniz---")
            sys.exit()

        p=input("deger giriniz : ")

        if not p in ("x","o"):
            print("x ya da o giriniz")
            sys.exit()
    
        else:
            xox[x][y]=p

            columns=[[xox[0][0],xox[1][0],xox[2][0]],
                     [xox[0][1],xox[1][1],xox[2][1]],
                     [xox[0][2],xox[1][2],xox[2][2]]]

            diagons  =[[xox[0][0],xox[1][1],xox[2][2]],
                       [xox[0][2],xox[1][1],xox[2][0]]]

            empty_points.remove([x,y])
            value_ai=random.choice(["x","o"])
            ai=random.choice(empty_points)
            xox[ai[0]][ai[1]]=value_ai
            empty_points.remove([ai[0],ai[1]])

        for i in xox:
            print(i)

        for i in xox:
            if set(i)==solution1 or set(i)==solution2:
                print("---tebrikler kazandınız---")
                return

        for i in columns:
            if set(i)==solution1 or set(i)==solution2:
                print("---tebrikler kazandınız---")
                return
        for i in diagons:
            if set(i)==solution1 or set(i)==solution2:
                print("---tebrikler kazandınız---")
                return

play()
