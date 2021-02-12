"""Write a function in Python PUSH(arr) where arr is list of numbers. from the list
push all numbers into a stack implemented by using alist. Display the stack
if it has at least one elements ,otherwise display appropriate error message
    Write a function POP(arr) where arr is stack implemented by the list of
numbers.the function return the value deleted from the stack"""

def PUSH(arr):
    s=[]
    for x in range(len(arr)):
        s.append(arr[x])
    if len(s)==0:
        print("Empty Stack")
    else:
        print(s)

def POP(arr):
    if len(arr)==0:
        print("Stack Empty")
    else:
        L=len(arr)
        no=arr[L-1]
        print(" Data Deleted :",no)
        arr.pop()
def peek(arr):
    l = len(arr)
    for i in range(l - 1, -1, -1):
        print(arr[i])


stack=[]
ch="Y"
while ch=='Y'or ch=='y':
    print("1..PUSH")
    print("2..POP")
    print("3..Display")
    choice=int(input("Your Choice"))
    if(choice==1):
        stack=eval(input("Enter list to push"))
        PUSH(stack)
    elif (choice==2):
        POP(stack)
    elif(choice==3):
        peek(stack)
    else:
        print("Wrong Input")
    ch=input("Do you want to continue or not ")


