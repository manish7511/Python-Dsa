num=int(input("enter a number: "))

if num==1:
    print("not a prime nor composite")

if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not a prime no")
            break
    else:
        print("prime no")