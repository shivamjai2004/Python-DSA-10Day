# Q.1
# import math
# input=[79,77,54,81,48,34,25,16]

# count =0
# for i in range(len(input)):
#     value = input[i]
#     root = math.isqrt(value)
#     if root*root == value:
#         count+=1

# print(count)

# count=0
# for i in range(len(input)):
#     value=input[i]
#     j=1
#     while j*j <=value:
#         if j*j == value:
#             count+=1
#             break
#     j+=1
# print(count)

# Q.2
# def func(val,val_list):
#     var =1
#     val_list[0]=44

# t=3
# list=[1,2,3]
# func(t,list)
# print(t,list[0])

# Q.3
# def f(i,values=[]):
#     values.append(i)
#     print(values)
#     return values

# f(1)
# f(2)
# f(3)

# Q.4

# fruit={}
# def addone(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1
# addone('Apple')
# addone("Banana")
# addone('apple')

# print(len(fruit))

''' Q.5 Write a program to accept student name and marks from the keyboard and 
create a dictionary. Also display student marks by student name'''

# import sys
# dict={}

# while True:
#     print('Pick Option')
#     print("1.for Adding the Student")
#     print("2.for Display")
#     print("3.for Exit")
#     choice = int(input("enter the Choice: "))

#     if choice == 1:
#         list=[]
#         name = input("Enter the name of Student: ")
#         subjects = int(input("How many subjects are there: "))

#         for i in range(0,subjects):
#             print(f"Enter the marks of subject Number {i+1} : ")
#             list.append(int(input()))

#         dict[name]=list

#     elif choice == 2:
#         print(dict)

#     elif choice == 3:
#         sys.exit()
#     else:
#         print("Invalid Option")

# Q.6 Forward printing Using while loop
# str = "Learning Python is very easy"
# length = len(str)
# i=0
# while i < length:
#     print(str[i],end="")
#     i+=1

# Q.7 Backward printing Using while loop
# str = "Learning Python is very easy"
# length = len(str)-1
# while length >= 0:
#     print(str[length],end="")
#     length-=1

# input ="abcdfiger abcdfger"
# output="j"

# list= input.split(" ")
# print(list)

# first =list[0]
# second=list[1]

# print(first)
# print(second)

# i=0
# j=0
# islast=True
# while(i < len(first) and j < len(second)):
#     if(first[i] != second[j]):
#         print(first[i])
#         islast=False
#         break
#     i+=1
#     j+=1

# if(islast):
#     print(first[-1])


# v=['a','e','i','o','u']
# input="shivam"
# found=[]
# for i in input:
#     if i in v:
#         if i not in found:
#             found.append(i)


# print(found)

# x,y,z = map(int,input().split())
# mylist=[]
# size = 6
# start=30
# end=50
# list=[29,38,12,48,39,55]

# for i in list:
#     if i >=start and i <=end:
#         print(i)



# import datetime

# date=datetime.datetime.now()
# print(date)

# print("{:%d/%m/%y}".format(date))
# print("{:%H:%M:%S}".format(date))

# x=['a','b']
# y=['a','b']
# z=[1,2]
# print(x==y)
# print(x==z)
# print(x != z)

# List Compression
# val=[2**i for i in range(1,6)]
# print(val)

# Dict Compression
# dict={x:x*x for x in range(1,6)}
# print(dict)

# a,b=[int(x) for x in input("Enter 2 Number: ").split()]
# print("Prod is ",a*b)

# a,b,c=[float(x) for x in input("Enter 3 Float: ").split(',')]
# print(a,b,c)

# myCart=[10,20,800,60,70]
# for item in myCart:
#     if item>400:
#         print("This is not in my Budget!!")
#         continue
#     print(item)
# else:
#     print("U have purchased everything")


# while True:
#     username=input("Enter username: ")
#     password=input("Enter password: ")

#     if(username == 'admin' and password == 'admin'):
#         print("Logged in successfully!!")
#         break
#     else:
#         print("Re-enter username and Password")

import time
class Tower:

    def __init__(self):
        print("Wel To Tower Of Hanoi")
        print()
        print("Given a probmelm A=[3,2,1] B=[] C=[]")
        print()
        print("Given a probmelm A=[] B=[] C=[3,2,1]")
        self.A=[3,2,1]
        self.B=[]
        self.C=[]
        
    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")
    
    def pass1(self):
        self.temp=self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A , "  ", "B=",self.B , "  ","C=",self.C)
        print("pass 1 Completed")
        
    
    def pass2(self):
        self.temp=self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A , "  ", "B=",self.B , "  ","C=",self.C)
        print("pass 2 Completed")

    def pass3(self):
        self.temp=self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A , "  ", "B=",self.B , "  ","C=",self.C)
        print("pass 3 Completed")
        
    def pass4(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A , "  ", "B=",self.B , "  ","C=",self.C)
        print("pass 4 Completed")


    def pass5(self):
        self.temp=self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A , "  ", "B=",self.B , "  ","C=",self.C)
        print("pass 5 Completed")

    def pass6(self):
        self.temp=self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A , "  ", "B=",self.B , "  ","C=",self.C)
        print("pass 6 Completed")

    def pass7(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A , "  ", "B=",self.B , "  ","C=",self.C)
        print("pass 6 Completed")

    
obj=Tower()
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

        