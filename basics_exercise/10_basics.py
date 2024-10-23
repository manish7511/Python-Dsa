def maximum(a,b,c):
    if (a>b) and a>c:
        return (a,"a is he largest")
    elif (b>a) and b>c:
        return (b ,"b is the largest")
    else:
        return (c,"c is the largest")
    

print(maximum(10,3,9))