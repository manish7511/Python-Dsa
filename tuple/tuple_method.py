# if you want to add,removeor change tuple items,
# then first you must convert he tuple to alist.then perform opertaion on that lists and convert it back to tuple.

countries=("spain","italy","india","usa")
temp=list(countries)
temp.append("russia") #add item
temp.pop(3)           #remove item
temp[2]="finland"     #change item
countries=tuple(temp)
print(countries)
print(type(countries))