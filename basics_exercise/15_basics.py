def check(num):
    if num==0:
        return num,"is zero"
    elif num>0:
        return (num,"is positive")
    else:
        return num,"is negative"
n=int(input("enter a number: "))   
print(check(n))