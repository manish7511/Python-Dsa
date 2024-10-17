m=[23,2,12,2,"manish"]

print(m)
print(m[2])
print(m[:])
print(m[1:-3])

m[0]=1
print(m)

# list comphersions

m=[i*i for i in range(4)]
print(m)
m=[i*i for i in range(9) if i%2==0]
print(m)