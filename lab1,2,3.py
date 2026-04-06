#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)


# In[7]:


no_of_terms = int(input("Enter number of values: "))
list1 = []

for val in range(0, no_of_terms, 1):
    ele = int(input("Enter integer: "))
    list1.append(ele)

print("Circulating the elements of list", list1)

for val in range(0, no_of_terms, 1):
    ele = list1.pop(0)
    list1.append(ele)
    print(list1)


# In[8]:


import math

p1 = [4, 0]
p2 = [6, 6]

distance = math.dist(p1, p2)
print(distance)


# In[9]:


a = 0
b = 1
n = int(input("Enter the number of terms in the sequence: "))

if n <= 0:
    print("Invalid input")
elif n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(n - 2):
        c = a + b
        print(c, end=" ")
        a, b = b, c


# In[11]:


for i in range(10):
    print(str(i) * i)


# In[14]:


def triangle(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print()

n = 5
triangle(n)


# In[15]:


rows = int(input("Enter number of rows: "))
k = 0
count = 0
count1 = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(" ", end=" ")
        count += 1

    while k != (2 * i - 1):
        if count <= rows - 1:
            print(i + k, end=" ")
            count += 1
        else:
            count1 += 1
            print(i + k - (2 * count1), end=" ")
        k += 1

    count1 = count = k = 0
    print()



# In[16]:


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

num = 5
print("Factorial of", num, "is", factorial(num))


# In[17]:


integers = [1, 16, 3, 39, 26, 4, 8, 16]

unique_list = list(set(integers))
largest = max(unique_list)
unique_list.remove(largest)
second_largest = max(unique_list)

print(largest)
print(second_largest)


# def areacalculator():
#     _input_ = input("Enter the shape you want to calculate area of: ").lower()
#     pie = 3.14
# 
#     if _input_ == "square":
#         side = int(input("Enter the value of side: "))
#         area = side ** 2
# 
#     elif _input_ == "circle":
#         radius = int(input("Enter the value of radius: "))
#         area = pie * radius * radius   # correct formula
# 
#     elif _input_ == "rectangle":
#         length = int(input("Enter the value of length: "))
#         width = int(input("Enter the value of width: "))
#         area = length * width
# 
#     elif _input_ == "triangle":
#         base = int(input("Enter the value of base: "))
#         height = int(input("Enter the value of height: "))
#         area = 0.5 * base * height
# 
#     else:
#         print("Select a valid shape")
#         return
# 
#     print("Area = %.2f" % area)
# 
# 
# areacalculator()

# In[ ]:




