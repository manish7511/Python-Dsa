# Write a program that takes a number as input and calculates its factorial using a loop.

num=int(input("enter the number: "))

fac=1

if num<0:
    print("factorial  is not defined for negative numbers")
elif num==0:
    print("factorail of 0 is 1")
else:
    for i in range(1,num+1):
        fac=fac*i
        print(fac)
    print(f"the factorial of {num} is {fac}")