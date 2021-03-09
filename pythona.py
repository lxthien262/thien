# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:09:30 2021

@author: DELL
"""
from file_thutu1 import thutu 
cot=int(input("so can nhap la :"))
matrix = []
print("nhap so  :")
for i in range(1):
    a=[]
    for j in range(cot):
        a.append(int(input()))
    thutu(a)
    matrix.append(a)
for i in range (1):
    for j in range(cot):
        print(matrix[i][j], end = "")