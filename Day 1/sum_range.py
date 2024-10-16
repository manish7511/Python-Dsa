# Create a program that takes two integers as input and prints the sum of all numbers between them (inclusive).

num1=int(input("enter th first number: "))
num2=int(input("enter the second number: "))

start=min(num1,num2)
end=max(num1,num2)


total_sum=0
for i in range(start,end+1):
    total_sum=total_sum+i

print(f"The sum of all numbers between {num1} and {num2} (inclusive) is: {total_sum}")