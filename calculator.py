
def cal():
    a = int(input("Enter the number: "))
    c = input("Enter the operation ")
    b = int(input("Enter the number: "))
    if c=='+':
        print(f"The sum of {a} and {b} is: ",a+b)
    elif c=='-':
        print(f"The difference of {a} and {b} is: ",a-b)
    elif c=='/':
        print(f"The division of {a} and {b} is: ",a/b)
    elif c=='*':
        print(f"The Multiplication of {a} and {b} is: ",a*b)
    elif c=='^':
        print(f"{b} to the power {a} is: ",a**b)
    else:
        print("please enter the right operation ")
    return cal()
cal()
