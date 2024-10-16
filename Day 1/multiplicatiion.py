num=int(input("enter the number: "))

print(f"multiplation table for {num}")
for i in range(1,11):
    result=num*i
    print(f"{num} * {i} is {result}")