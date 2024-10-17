# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#         print (sum/len(numbers))

# average(5,6)

# def name(*name):
#     print("hello",name[0],name[1])

# name("manish","singh")

def name(**name):
    print("hello",name["fname"],name["lname"])

name(lname="singh",fname="manish")