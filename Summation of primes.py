# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 00:45:02 2020

@author: Ajay
"""
if __name__ == "__main__":
    x=[]
    t=[]
    p=2
    count=0
    
    for i in range(2,2000000):
        x.append(i)
    
    while len(x)!=1:
        for i in x:
            if i%p==0:
                x.remove(i)
        t.append(p)    
        p=x[0]
        count=count+1
    print(sum(t))