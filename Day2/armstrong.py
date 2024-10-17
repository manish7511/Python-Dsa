num=int(input("enter a number: "))
sum=0
temp=num

while temp>0:
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp=temp//10

if sum==num:
    print("this is armstrong number")
else:
    print("this is not armstrong number")

