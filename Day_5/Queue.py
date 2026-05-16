#queue datastructure
# 1. EnQueue --> Add element
# 2. DeQueue --> Delete element
# 3. Display Queue
# 4. IsEmpty
# 5. IsFull()
# 6. Delete
# 7. Queue

# Stack using List
# 1.Easy to implement 
# 2.slow when n is large

# Stack using LinkedList
# 1.Diff to Implement
# 2.Fast

import sys
class Queue:
    def __init__(self,size):
        self.myQueue=[]
        print(f"The queue has been created with size {size}")
        

    def insert(self,key,size):
        if len(self.myQueue) == size:
            print("Queue is full !!")
        else:
            self.myQueue.append(key)
            print('Element has been inserted: ')

    def display(self):
        print(self.myQueue)

    def delete(self):
        if self.myQueue == []:
            print("Queue is Empty !!")
        else:
            self.myQueue.remove(self.myQueue[0])

    def deleteQueue(self):
        self.myQueue=None
        print("Queue has been Deleted!!")

    def peek(self):
        if self.myQueue == []:
            print("Queue is Empty!!")
        else:
            print(self.myQueue[0])


size= int(input("Enter the size of Queue: "))
queue = Queue(size)
while True:
    print("1.Insert Element")
    print("2.Delete Element")
    print("3.Display")
    print("4.Delete Queue")
    print("5.Peek the Front Element")
    print("7.Exit")

    choice = int(input("Enter the choice: "))
    if(choice == 1):
        value = int(input("Enter the key: "))
        queue.insert(value,size)
    elif(choice == 2):
        queue.delete()

    elif(choice == 3):
        queue.display()
    elif choice == 4:
        queue.deleteQueue()
    elif choice == 5:
        queue.peek()
    elif choice == 7:
        sys.exit()
    else:
        print('Invalid Choice!!')
