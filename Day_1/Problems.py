# day = input("Enter the Current Day: ")
# day = day.lower

# if(day == "sunday" or day == "saturday"):
#     print("Not Working day")

# else:
#     print("Working Day")


# ch = ord(input("Enter the Character: "))

# if(ch >= 65 and ch <= 90):
#     print("The Character is UpperCase")

# elif (ch >= 97 and ch <= 122):
#     print("The charcater is Lower Case")

# elif(ch >= 48 and ch <= 57):
#     print("The character is Digit")

# else:
#     print("The char is special symbol")


# list = [0,1,4,0,2,5]
# left=0
# right=len(list)-1
# while left < right:
#     if(list[right]==0):
#          right-=1
#     elif(list[left]==0):
#         temp=list[right]
#         list[right]=list[left]
#         list[left]=temp
#         right-=1  
#         left+=1
#     else:
#         left+=1

# print(list)

# list = [7,3,9,2,8]
# max1=-1
# max2=-1

# for i in list:
#     if(i > max1):
#         max2=max1
#         max1=i

# print(max2)

#Q.2
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# Q.3
# a=[1,2,3,4,5]
# print(a[3:0:-1])

# Q.4
# arr=[
#     [1,2,3,4],
#     [4,5,6,7],
#     [8,9,10,11],
#     [12,13,14,15]
#     ]

# for i in range(0,4):
#     print(arr[i].pop())

# Q.5
# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]

# for i in range(0,6):
#     print(arr[i], end=" ")

# Q.6
# f1 =['A','B','C','P']
# f2=f1
# f3=f1[:]
# f2[0]='G'
# f3[1]='K'

# sum=0
# for ls in (f1,f2,f3):
#     if ls[0]== 'G':
#         sum+=1
#     if ls[1] == 'K':
#         sum+=20

# print(sum)

# a=[1,2,3]
# b=[2,3,4]
# c=[3,4,5]

# for i in a:
#     if i in b and i in c:
#         print(i)

size = int(input("Enter the sie of array: "))
mylist=[]
for i in range(0,size):
    value= int(input("Enter the digit :"))
    mylist.append(value)


sum =0
for i in range(0,size-1):
    if(mylist[i] > mylist[i+1]):
      sum = sum + mylist[i]-mylist[i+1]
    else:
       sum = sum + mylist[i+1] - mylist[i]

print(sum)