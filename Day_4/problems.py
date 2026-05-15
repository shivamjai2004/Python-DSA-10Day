# #Q.1
# input = "aaabbbbccceeeee"
# dict={}
# for i in input:
#     count=0
#     char=i
#     for j in input:
#         if(i == j):
#             count+=1

#     dict[char]=count
# print(dict)

# for i in dict:
#     print(i,dict[i],sep='',end='')

#Increment the salary of emp based on rating

# salary=int(input("Enter the salary of emp: "))
# rating = int(input("Entere the rating of emp: "))
# increment=0

# if rating >=1 and rating <=3:
#     increment = salary*10/100
#     print(f"Inc Salary : {salary+increment}")
# elif rating >3 and salary <=4:
#     increment = salary*30/100
#     print(f"Inc Salary : {salary+increment}")
# elif rating > 4 and salary <=5:
#     increment = salary*40/100
#     print(f"Inc Salary : {salary+increment}")
# else:
#     print("Invalid Rating")


# Calculate the gross salary

# baseSalary = int(input('Entere the basic salary: '))
# hra= baseSalary * 20/100
# ta= baseSalary * 30/100
# da= baseSalary * 45/100
# Gross = baseSalary + hra + ta + da
# print(f"Gross : {Gross}")




