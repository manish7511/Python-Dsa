num1=int(input("enter number: "))
num2=int(input("enter number: "))
num3=int(input("enter number: "))

if (num1>num2) and (num1>num3):
    print(num1," num1 is greater")
elif (num2>num3) and (num2>num1):
    print(num2," num2 i greater")
else:
    print(num3,"num3 is greater")