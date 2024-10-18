# string fromatting

letter="my name is {1} i am from {0}"
name="manish"
place="muzaffarpur"
print(letter.format(place,name))


# fstrings

print(f"my name is {name} and i am from {place}")
print(f"my name is {{name}} and i am from {{place}}")