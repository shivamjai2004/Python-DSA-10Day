# #Q.1 remove duplicate from string 
# name="prashant"
# new=""
# # length = len(name)
# for i in name:
#     if i not in new:
#         new= new + i           
# print(new)

# #Q.2 reverse using function
# reverse=new[::-1]

#Q.3 reverse using reverse for loop
# reverse=""
# length = len(new)
# for i in range(length-1,-1,-1):
#     reverse+=new[i]
# print(reverse)

#Q.4 Check for palindrome

# name = "madam"

# left=0
# right=len(name)-1

# while(left<right):
#     if(name[left] != name[right]):
#         print("Not Palindrome")
#         break
#     left+=1
#     right-=1
# print("Palindrome")

# Q.5 Count Vowels and consonenet

# name="prashant"
# name=name.lower()
# vowel=0
# consonent=0
# for i in name:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
#         vowel+=1
#     else:
#         consonent+=1

# print(f"{vowel} Vowel Count and {consonent} consonent Count")

# Q.6 Check for Anagram

# s="listen"
# t="silent"
# boolean=True
# if(len(s) != len(t)):
#     print("Not an Anagram")
# else:
#     list=[]
#     list.append(s)
#     for i in t:
#         if(i in list):
#             list.remove(i)
#         else:
#             print("Not Anagram")
#             boolean=False
#             break
# if(boolean):
#     print("Anagram")

# Q.10 Count Words in a String

# input ="this is a sentence"
# input=input.lower()
# input=input+" "
# length = len(input)
# left=0
# right=0
# count=0
# for i in input(0,length):
#     if(ord(right[i]) >= 97 and ord(right[i]) <=121):
#         right+=1
#     else:
#         count+=1

# print(count)

# a=50
# b=30
# c=20
# d=10

# print((a+b)*c/d)

# Q.11 find the number of Special symbol and whitespaces
# str = "gasgg54@#vscsd!s "
# count=0
# for i in str:
#     num = ord(i)
#     if(num >= 97 and num <= 122 or num >=48 and num <= 57 ):
#         continue
#     else:
#         count+=1

# print(count)

# Q.12 Title case a Sentence

# input = "this is a test"
# input=input.title()
# print(input)

# Q.13 Printing patterns
# 1 1 1
# 2 2 2
# 3 3 3

# n=3
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()

# Q.14 Printing patterns
# n =5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=' ')
#     print()


# Q.15 Printing patterns
# n =5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=' ')
#     print()


# Q.16 Printing patterns
# n =5
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print("*",end=' ')
#     print()


# Q.17 Printing patterns
# n =5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()


# Q.18 Printing patterns
# import time
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(2)
#         print("*",end=' ')
#     print()

# Q.19 Product of array except self

# prod=1
# list=[1,2,3,4]
# for i in list:
#     prod=prod*i

# for i in range(0,len(list)-1):
#     list[i]=prod/list[i]

# for i in list:
#     print(int(i)," ",end=" ")

# dict={
#     "A":50,
#     "B":30,
#     "C":70
# }
# max=-1000
# key=0
# for i in dict:
#     if dict[i] > max:
#         max=dict[i]
#         key=i

# print(key)


# dict={
#     "X":20,
#     "Y":10,
#     "Z":30
# }
# min=5000
# key=0
# for i in dict:
#     if(dict[i] < min):
#         min=dict[i]
#         key=i
# print(key)

# list=[1,2,2,3,4,3,5]
# set={}
# for i in list:
#     set.add(i)
# dict={}
# for i in set:
#     val =i
#     countof=list.count(val)
#     dict[i]=countof

# print(dict)


num=123456
rev=0
while(num > 0):
    rev= rev*10 + num%10
    num=num//10

print(rev)

amount=753

print("Note of 100rs: ",amount//100)
print("Note of 50rs: ",(amount%100)//50)
print("Note of 20rs: ",((amount%100)%50)//20)
print("Note of 10rs: ",(((amount%100)%50)%20)//10)
print("Note of 5rs: ",((((amount%100)%50)%20)%10)//5)
print("Note of 2rs: ",(((((amount%100)%50)%20)%10)%5)//2)
print("Note of 1rs: ",((((((amount%100)%50)%20)%10)%5)%2)//1)



