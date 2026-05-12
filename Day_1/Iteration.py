# for i in range(1,6,2): #default 0
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# for i in range(1,11):
#     print()
#     for j in range(2,21):
#         print(i*j,end=' ')


# eng =int(input("Enter the marks of English Subject: "))
# chem=int(input("Enter the marks of Chem Subject: "))
# math=int(input("Enter the marks of Math Subject: "))
# gender = input("Enter your Gender: ")
# total = eng+chem+math
# per=total/300*100
# if(eng >= 40 and chem >= 40 and math >= 40):
#       print("Passed in all Subject")
# else:
#       print("Failed")
      

# if(per>= 65 and gender == "male" or gender == "MALE" ):
#         print("eligible for Placement")
# else:
#     print("Not eligible for Placement")

n = 6
last = 6
for i in range(1,n):
    last-=1
    if(i == 3 and last == 3):
        continue
    print(i," ",last)
