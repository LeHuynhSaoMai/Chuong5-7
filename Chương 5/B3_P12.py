# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 23:32:09 2024

@author: Smai
"""

import random

# Chọn số lượng phần tử ngẫu nhiên từ 20 đến 30
a = random.randint(20, 30)

# Khởi tạo danh sách với kích thước a
pt = [0] * a 

for i in range(a):
    # Chọn số thực ngẫu nhiên từ 18 đến 99
    so_t = random.uniform(18, 99)
    pt[i] = so_t ** 2  # Gán giá trị bình phương vào danh sách

# In danh sách kết quả
print("Số lượng phần tử: ", a)
print("Danh sách các giá trị bình phương:", pt)