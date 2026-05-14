#While loop
# i=1
# while i<=5:
#     print(i)
#     i+=1

#function

# def hello():
#     print("Hello World!")

# hello()
# hello()

# def arithmetic():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b: "))
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub,mul,div #Tuple

# result = arithmetic()
# print(result[0])

# How Many types of argument we pass in function
# 1.Positional argument

# def arithmetic(a,b):
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub,mul,div #Tuple

# result = arithmetic(5,5)
# print(result[0])


# 2.KeyWord argument

# def credential(username,password):
#     if(username == "admin" and password =="123"):
#         print("Login Successfully")
#     else:
#         print("Wrong Credentials")

# credential(username="admin",password="123")


# 3.default argument


# def cityName(city="pune"):
#     print(city)

# print("ngp")
# print("mumbai")
# print()


# 4.variable length argument/ variable number of argument

# def cityName(*name):
#     print(name)

# cityName("Ngp","pune","mumbai")



#Modularity approach  in function
import sys
def sum():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b: "))
    return (a+b)

def div():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b: "))
    return (a/b)

def mul():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b: "))
    return (a*b)

def sub():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b: "))
    return (a-b)


while True:
    print("1 for addition")
    print("2 for substraction")
    print("3 for division")
    print("4 for multiplication")
    print("5 for exit")
    choice = int(input("Enter the Choice: "))

    if(choice == 1):
        res = sum()
        print(res)
    elif choice == 2:
        res = sub()
        print(res)

    elif choice == 3:
        res = div()
        print(res)

    elif choice == 4:
        res = mul()
        print(res)

    elif choice == 5:
        sys.exit()
    else:
        print("wrong choice")
