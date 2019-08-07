# -*- coding: utf-8 -*-
"""
Created on Fri May 11 09:55:21 2018

@author: MR
"""

#3d6
import matplotlib.pyplot as plt
i=j=k=1
p=0
tot=[]
prob=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

while i<7:
    j=1
    while j<7:
        k=1
        while k<7:
            tot.append(i+j+k)
            k+=1
        j+=1
    i+=1
    
while p<len(tot):
    prob[tot[p]-3]+=1
    p+=1
    
plt.plot(x,prob)
plt.grid()
plt.show()
print('Value\t',x,'\nChance\t',prob)
print('Sum\t',len(tot))
