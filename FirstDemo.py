print("HELLO")

# This is my first comment

a = 3
b = 4
c= a+b

print(c)

Str = "Hello World"

print(Str)

d, e, f = 10, 12.5, "ABC"
print(d, e, f)

# print("Value is"+b) - This isn't possible in python - TypeError: can only concatenate str (not "int") to str
print("{} {}".format("Value is", b))

print(type(d))
print(type(e))
print(type(f))

text1 = "This is string1"
text2 = "This is string2"
print(text1 + " concatenates " + text2) # Concatenation of same datatype is possible in Python
