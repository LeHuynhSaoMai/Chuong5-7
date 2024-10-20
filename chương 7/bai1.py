# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:32:20 2024

@author: smai
"""

def tong_tich(*args, **kwargs):
    a = sum(args)
    b = 1
    for i in args:
        b *= i
    return a, b
tong,tich = tong_tich(28,7,5)
print("Tổng =",tong)
print("Tích =",tich)