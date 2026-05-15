# def bubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 temp=array[j]
#                 array[j]=array[j+1]
#                 array[j+1]=temp

#     print(array)

# array=[64,34,25,12,22,11,90]
# print(array)
# bubbleSort(array)

# Q. A comp wants to transmit the data and security key
# input=5783789223
# output=4

input=str(5783789223)
dict={}
for i in range(0,len(input)):
    for j in range (i+1,len(input)):
        if(input[i] == input[j]):
            dict[i]=0
if(len(dict) >= 1):
    print(len(dict))
else:
    print(-1)