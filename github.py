# -*- coding: utf-8 -*-
"""
Created on Fri May  3 01:13:29 2019

@author: Batuhan
"""

#calculate pi value according to leibniz equation

def pi(x):
    pi=1
    for i in range(0,x):
        j=i*2+3
        if i%2==0:
            pi=pi-1/j
        else:
            pi=pi+1/j
    return pi*4


pi(10000)

--------------------------------

#basic form application to practice on string methods and list

import sys
mylist={}
def login():
    name=input("İsim giriniz : ")
    if any(i.isdigit() for i in name):
        sys.exit("Sadece karakter giriniz")
    surname=input("Soyisim giriniz : ")
    if any(i.isdigit() for i in surname):
        sys.exit("Sadece karakter giriniz")
    email=input("Email giriniz : ")
    if not (email.count("@")==1 and email.count(".")):
        sys.exit("'@' ,'.' karakteri kullanımı hatası")
    if any(i==email for i in mylist.keys()):
        sys.exit("Bu email adresi zaten kayıtlı")
    password=input("Parola oluşturunuz : ")
    if not any(i.islower() for i in password):
        sys.exit("En az bir küçük harf giriniz.")
    if not any(i.isupper() for i in password):
        sys.exit("En az bir büyük harf giriniz.")
    if not any(i.isdigit() for i in password):
        sys.exit("En az bir rakam giriniz.")
    if len(password)<8:
        sys.exit("En az 8 karakter giriniz.")
    else:
        mylist[name]=surname
        mylist[email]=password
        print("{} {} adlı kullanıcı {} adresi ile giriş yaptı".format(name,surname,email))
    
login()

------------------

#code to find prime numbers until x

def prime(x):
    prime_numbers=[]
    for i in range(2,x):
        if any(i%j==0 for j in range(2,i)):
            continue
        else:
            prime_numbers.append(i)
    print(prime_numbers)
                
prime(100)


-----------

#code to print fibonacci numbers until x and calculate golden ratio

def fibo(x):
    golden=[]
    numbers=[]
    a,b=0,1
    for i in range(x):
        a,b=b,a+b
        c=b/a
        numbers.append(a)
        if a==0:
            continue
        else:
            golden.append(c)

    for i in golden:
        print(i)
    print(numbers)



fibo(29)

---------------

#multiplication of every mylist element except "i" element

def multiple():
    mydict={}
    mylist=[]
    x=int(input("sayi giriniz : "))
    mylist.append(x)
    y=int(input("sayi giriniz : "))
    mylist.append(y)
    z=int(input("sayi giriniz : "))
    mylist.append(z)
    w=int(input("sayi giriniz : "))
    mylist.append(w)
    for i in mylist:
        times=1
        for j in mylist:
            if i==j:
                continue
            else:
                times=times*j
        mydict[i]=times
    print(mylist)
    print(mydict)
    
multiple()

-----------


#x is perfect number or not

def mukemmel(x):
    dizi=[]
    for i in range(1,x):
        toplam=0
        for j in range(1,i):
            if i%j==0:
                toplam=toplam+j
        if toplam==i:
            dizi.append(i)
    print(dizi)
    
mukemmel(500)


--------------------

#find the random number
    
import random
def sayibul(n):
    y=random.choice(range(n))
    while True:
        x=int(input("sayi giriniz : "))
        if x>y:
            print("daha küçük sayı girin")
        elif x==y:
            print("tebrikler sayı : ",y)
            return
        else:
            print("daha büyük sayı giriniz")   
sayibul(49)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















