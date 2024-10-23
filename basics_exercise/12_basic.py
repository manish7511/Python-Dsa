def km_to_miles(km):
    miles=km*0.62137
    return miles

KM=float(input("enter a km :"))

print(f"{KM} kilometer is {km_to_miles(KM)} miles")