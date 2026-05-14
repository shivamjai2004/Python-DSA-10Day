# Ds are different ways of organizing data on your computer

# Time Complexity

# O(1) Constant [accesing an element of an array]
# O(logN) Logarithmic [Binary Search]
# O(N) Linear [Traversing an array]
# O(N^2) Quadratic [looking at every index in an array twice]
# O(2^N) Exponential [fibonacci or Tree prob]

#Find MaXiMuM number

# def findBig(arr): #=======> O(1)
#     max = arr[0]  #=======> O(1)
#     for i in range(1,len(arr)):#=======> O(N)
#         if arr[i] > max: #=======> O(1)
#             max=arr[i]   #=======> O(1)
#     return max   #=======> O(1)


# arr=[1,2,3,4,5,6,7,14,2,15] #=======> O(1)
# result = findBig(arr) #=======> O(1)
# print(f"The maximum element in list is: {result}") #=======> O(1)

#OVERALL => O(N)

# def linearSearch(array,target):
#     for i in range(0,len(array)):
#         if(array[i] == target):
#             return i
#     return -1
        

# list=[1,2,3,4,5,6,7,8]
# key=2
# index = linearSearch(list,key)
# if(index != -1):
#     print(f"The element is present at index {index}")
# else:
#     print("Not found")


#Row wise Max

# grid = [
#     [100,198,333,323],
#     [122,232,221,111],
#     [223,565,245,764]
# ]
# row = len(grid)
# col = len(grid[0])

# for i in range(0,row):
#     max=0
#     for j in range(0,col):
#         if(grid[i][j] > max):
#             max=grid[i][j]

#     print(f"Max element in row {i+1} is :",max)

#shift stars at the start
# input= "prashant*is*a*good*programmer"
# Stars=""
# newString=""
# for i in input:
#     if(i =='*'):
#         Stars+="*"
#     else:
#         newString+=i

# print(Stars+newString)


# input = aaabbbbccceeeee
# output = a3b4c3e4
# dict={}





