dic={
    "manish":"human",
    "spoon":"object",
    "country":"india"
}
# print(dic["manish"])
# print(dic.get('name2'))
# print(dic.get("manish"))


# for key in dic.keys():
#     print(f"The value of corresponding to the key {key} is {dic[key]}")

print(dic.items())
for key,value in dic.items():
    print(f"The value of corresponding to the key {key} is {value}")