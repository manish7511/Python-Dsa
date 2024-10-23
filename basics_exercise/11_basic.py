def simple_intrest(p,t,r):
    si=(p*t*r)/100
    return si
P = int(input("Enter the principal amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))

print("simple intrest is",simple_intrest(P,T,R))