num1=int(input("enter a number:"))
num2=int(input("enter a number:"))

start=min(num1,num2)
end=max(num1,num2)

total_sum=0

for i in range(start,end+1):
    total_sum+=i

print(total_sum)