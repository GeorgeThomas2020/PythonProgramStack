stack=[]
ch="Y"
while ch=='Y'or ch=='y':
    print("1..PUSH")
    print("2..POP")
    print("3..Display")
    choice=int(input("Your Choice"))
    if(choice==1):
        num=input("Enter Number")
        stack.append(num)
    elif (choice==2):
        if(stack==[]):
            print("Stack Empty")
        else:
            print("Deleted  element is",stack.pop())
    elif(choice==3):
        l = len(stack)
        for i in range(l - 1, -1, -1):
            print(stack[i])
            # can write print(stack[::-1]
    else:
        print("Wrong Input")
    ch=input("Do you want to continue or not ")


