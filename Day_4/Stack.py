# there are 2 ways to implement stack
# 1.List
# 2.LinkedList
# import sys
# class Stack:
#     def __init__(self):
#         self.myStack=[] # Creating a stack
#     def push(self,value):
#         self.myStack.append(value)
#         print('Element has been pushed')
        
#     def display(self):
#         print(self.myStack)
    
#     def pop(self):
#         if(self.myStack != []):
#             self.myStack.pop()
#             print("Element has been popped!!")
#         else:
#             print("Stack is Empty!!")
#     def isEmpty(self):
#         if(self.myStack == []):
#             print("The Stack is Empty!!")
#         else:
#             print("The Stack is not Empty")
#     def peek(self):
#         if(self.myStack == []):
#             print("The Stack is Empty!!")
#         else:
#             print(self.myStack[-1])
#     def delete(self):
#         self.myStack=None
#         print("Stack has been removed!!")


# obj = Stack()

# while True:
#     print("1.Push")
#     print("2.Display")
#     print("3.pop")
#     print("4.IsEmpty Status")
#     print("5.Peek")
#     print("6.Delete stack")
#     print("7.Exit")

#     choice=int(input("Enter the choice: "))

#     if(choice == 1):
#         key = int(input('enter the value: '))
#         obj.push(key)
#     elif(choice == 2):
#         obj.display()
#     elif(choice == 3):
#         obj.pop()
#     elif(choice == 4):
#         obj.isEmpty()
#     elif(choice == 5):
#         obj.peek()
#     elif(choice == 6):
#         obj.delete()
#     elif(choice == 7):
#         sys.exit()
#     else:
#         print("Invalid Choice")


# Stack with Size Limitl

# import sys
# class Stack:
#     def __init__(self,size):
#         self.myStack=[size] # Creating a stack
#         print(f"Stack has been created with size {size}")

#     def push(self,value,size):
#         if (len(self.myStack) == size):
#             print("The stack is full")
#         else:
#             self.myStack.append(value)
#             print('Element has been pushed')
        
#     def display(self):
#         print(self.myStack)
    
#     def pop(self):
#         if(self.myStack != []):
#             self.myStack.pop()
#             print("Element has been popped!!")
#         else:
#             print("Stack is Empty!!")
#     def isEmpty(self):
#         if(self.myStack == []):
#             print("The Stack is Empty!!")
#         else:
#             print("The Stack is not Empty")
#     def peek(self):
#         if(self.myStack == []):
#             print("The Stack is Empty!!")
#         else:
#             print(self.myStack[-1])
#     def delete(self):
#         self.myStack=None
#         print("Stack has been removed!!")

# size = int(input("Enter the size of Stack: "))
# obj = Stack(size)

# while True:
#     print("1.Push")
#     print("2.Display")
#     print("3.pop")
#     print("4.IsEmpty Status")
#     print("5.Peek")
#     print("6.Delete stack")
#     print("7.Exit")

#     choice=int(input("Enter the choice: "))

#     if(choice == 1):
#         key = int(input('enter the value: '))
#         obj.push(key,size)
#     elif(choice == 2):
#         obj.display()
#     elif(choice == 3):
#         obj.pop()
#     elif(choice == 4):
#         obj.isEmpty()
#     elif(choice == 5):
#         obj.peek()
#     elif(choice == 6):
#         obj.delete()
#     elif(choice == 7):
#         sys.exit()
#     else:
#         print("Invalid Choice")

#Q
# input = 572378233
# digit = 3

# input=str(input)
# count=0
# for i in input:
#     if i == str(digit):
#         count+=1
# print(count)




