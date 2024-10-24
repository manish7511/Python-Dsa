for num in range(20,40):
    if  num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,"is prime")