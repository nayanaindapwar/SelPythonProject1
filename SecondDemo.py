# List declaration
values = [1, 2, "abc", 3, 4] # index : 0, 1, 2, 3, 4

# retrieve the variable values
print(values[0])
# output of above is 1

print(values[3]) # 3
print(values[-1]) # 4
print(values[1:3]) # 2, abc

# Insert
values.insert(3, "xyz")
print(values) # [1, 2, 'abc', 'xyz', 3, 4]

# Append : Append will add new variable at the end
values.append("end")

print(values) # [1, 2, 'abc', 'xyz', 3, 4, 'end']

# Update
values[2] = "ABC"
print(values) # [1, 2, 'ABC', 'xyz', 3, 4, 'end']

# Delete
del values[0]
print(values) # [2, 'ABC', 'xyz', 3, 4, 'end']

# Tuple declaration - Immutable - locked - we can't update/change it
val = (10, 20, "pqr", 30, 40)
print(val)

# val[2] = "PQR" - This isn't possible in python - TypeError: 'tuple' object does not support item assignment


# Dictionary Declaration
dic = {1: "first name", 2: "last name", "age": 33}
print(dic[1]) # first name
print(dic[2]) # last name
print(dic["age"]) # 33
print("Printing Dictionary Dic")
print(dic) # {1: 'first name', 2: 'last name', 'age': 33}

# Adding elements in empty dictionary
testDic = {}
testDic["First Name"] = "David"
testDic["Last Name"] = "Coe"
testDic["Gender"] = "Male"
print("Printing Dictionary testDic")
print(testDic) # {'First Name': 'David', 'Last Name': 'Coe', 'Gender': 'Male'}
print(testDic["Last Name"]) # Coe