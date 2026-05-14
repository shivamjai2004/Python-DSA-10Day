# # Q.18 Maximum Consecutive 1's

# list=[1,1,0,1,1,1,0,1,1,1,1]
# count=0
# maxCount=0
# for i in list:
#     if(i == 0):
#         count=0

#     else:
#         count+=1
#         maxCount=max(count,maxCount)

# print(maxCount)

# Q.19 

# input="abababab"
# substring="ab"
# left=0
# right=1
# count=0
# while(right< len(input)):
#     str=input[left:right+1]
#     if(str == substring):
#         count+=1
#     right+=1
#     left+=1

# print(count)