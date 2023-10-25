# String Operations
str = "Welcome to the world of Python"
str1 = " And Selenium"
str2 = "Python"
str3 = " Programming "

print(str[1])   # e
print(str[0:7])   # Welcome
print(str+str1)    # Welcome to the world of Python And Selenium --> Concatination
print(str2 in str)   # Ture --> Substring Check

var = str.split(" ")  # Split the string on the basis space (or any character)
print(var)  # ['Welcome', 'to', 'the', 'world', 'of', 'Python']
print(var[0])   # Welcome
print(str3.strip())   # Removing the white spaces
print(str3.lstrip())  # Removing the left spaces
print(str3.rstrip())  # Removing the right spaces