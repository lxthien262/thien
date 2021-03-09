# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:21:32 2021

@author: DELL
"""
def thutu(num): 
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(num)-1):
            if num[i]>num[i+1]:
                num[i],num[i+1]=num[i+1],num[i]
                swapped = True
         
    
