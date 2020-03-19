# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 03:36:25 2020

@author: Ajay
"""
import math 
def even(n):
    return math.floor(n/2)
def odd(n):
    return (3*n)+1

if __name__=="__main__":
    max_number=13
    max_count=10
    n=13
    while(n!=1000000):
            count=0
            ret=0
            temp=n
            while n!=1:
                if n%2==0:
                    n=even(n)
                    count=count+1
                else : 
                    n=odd(n)
                    count=count+1
            if max_count<count:
                max_count=count+1
                max_number=temp
            n=temp
            n=n+1
    print(max_number)