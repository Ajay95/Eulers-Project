# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 07:03:55 2020

@author: Ajay

https://www.mathsisfun.com/numbers/pythagorean-triples.html
Constructing Pythagorean Triples
It is easy to construct sets of Pythagorean Triples.

When m and n are any two positive integers (m > n):

a = m2 − n2
b = 2mn
c = m2 + n2
Then a, b, and c form a Pythagorean Triple.

Example: m=2 and n=1
a = 22 − 12 = 4 − 1 = 3
b = 2 × 2 × 1 = 4
c = 22 + 12 = 4 + 1 = 5
Thus, we obtain the first Pythagorean Triple (3,4,5).
"""
def triplets():
    x=[]
    for i in range(500):
        for j in range(500):
            if i*(i+j)==500:
                x.append(((pow(j,2)-pow(i,2)),(2*i*j),(pow(i,2)+pow(j,2))))
                break
    return(x)
if __name__=="__main__":
    x=triplets()
    for i in x:
        a,b,c=i
        if(abs(a)+abs(b)+abs(c)==1000):
            print(abs(a),abs(b),abs(c))
            print(abs(a)*abs(b)*abs(c))