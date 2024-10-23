# def swap(a,b):
#     print(f"before swapping tha value of a {a} and b is {b}")
#     a,b=b,a
#     print(f"before swapping tha value of a {a} and b is {b}")

# swap(2,3)

def swap(a,b):
    print(f"before swapping the value of a is {a} and b is {b}")
    temp=a
    a=b
    b=temp
    print(f"after swaping the value of a {a} and b is {b}")

swap(3,4)