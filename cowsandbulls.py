# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:14:04 2019

@author: Batuhan
"""

import random
def cowsnbulls():
    x=random.randrange(1000,10000)
    while not len(set(str(x)))==4:
        x=random.randrange(1000,10000)
        if len(set(str(x)))==4:
            break
    while True:
        listx=list(str(x))
        y=list(input("4 basamaklı bir sayı giriniz : "))
        n=0
        m=0
        for i in listx:
            for j in y:
                if i==j and listx.index(i)==y.index(j):
                    n=n+1
                if i==j and not listx.index(i)==y.index(j):
                    m=m+1
        print(n,"cows")
        print(m,"bulls")
        if n==4:
            print("Tebrikler sayi : ",x)
        if y==["q"]:
            return


cowsnbulls()