# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:16:34 2024

@author: User
"""

def kiemtra_giatri():
    n = input("Nhập n: ")
    if n.replace('.','',1).replace('-','',1).isdigit():
        n = float(n)
        if -89 <= n <= 90:
            return n
        print ("Không hợp lệ, nhập lại: ")
        return kiemtra_giatri()
if __name__=="__main__":
    print(kiemtra_giatri())