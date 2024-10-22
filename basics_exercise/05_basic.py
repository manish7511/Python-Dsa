def leap_year(year):
    if (year%4==0) and (year%100!=0 or year%400):
        print(year," is leap")
    else:
        print(year,"is not leap")
leap_year(1902)

number=1200
width = bin(number)
print(width)