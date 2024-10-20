# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:27:35 2024

@author: Smai
"""

n = int (input(" Nhập một số nguyên dương: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i
print ("S=n!", giai_thua)
