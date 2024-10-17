# Python Tuple is a collection of objects separated by commas.
#  In some ways, a tuple is similar to a Python list in terms of indexing, nested objects, 
# and repetition but the main difference between both is Python tuple is immutable, unlike the Python list which is mutable.

var = ("Geeks", "for", "Geeks")
print(var)

tup=("manish",1,2,3)
print(tup)
print(type(tup))

# tuple1[1] = 100
# TypeError: 'tuple' object does not support item assignment

tupl=(1,2,3,4,5)
print(tupl[1])
print(tupl[2])
print(tupl[-2])

if 4 in tupl:
    print("yes 4 in tupl")