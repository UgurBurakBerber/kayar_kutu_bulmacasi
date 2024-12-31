#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:10:53 2024

@author: ugurburak
"""
import numpy as np
import matplotlib.pyplot as plt

n = 4

a = np.arange(n*n)
np.random.shuffle(a)
a=a.reshape(n, n)
hedef = np.arange(n*n)
hedef = hedef.reshape(n, n)

s= [] #yığın, stack
s.append(a)
Liste = []
Liste.append(a)

while len(s) > 0:
    ata = s.pop()
    if np.all(ata==hedef):
        print(hedef)
        continue
    
    [y,x] = np.where(ata==0)
    y=y[0]
    x=x[0]
    
    if y > 0:
        yavru = np.copy(ata)
        yavru[y,x] = yavru [y-1,x]
        yavru[y+1, x] = 0
        if yavru not in Liste :
            Liste.append(yavru)
            s.append(yavru)
            
    if y < n-1:
        yavru = np.copy(ata)
        yavru[y,x] = yavru [y+1,x]
        yavru[y-1,x] = 0
        if yavru not in Liste :
            Liste.append(yavru)
            s.append(yavru)
            
    if x > 0:
        yavru = np.copy(ata)
        yavru[y,x] = yavru [y,x-1]
        yavru[y,x-1] = 0
        if yavru not in Liste :
            Liste.append(yavru)
            s.append(yavru)
            
    if x > n-1:
        yavru = np.copy(ata)
        yavru[y,x] = yavru [y,x+1]
        yavru[y,x+1] = 0

        if yavru not in Liste :
            Liste.append(yavru)
            s.append(yavru)        
    

