def smallest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1," num1 is greater"
    elif num2>num1 and num2>num3:
        return num2," num2 is greater"
    else:
        return num3,"num3 is greater"
    
num1=int(input("enter a num1: "))
num2=int(input("enter a num2: "))
num3=int(input("enter a num3: "))

print(smallest(num1,num2,num3))