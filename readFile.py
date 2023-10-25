# We'll learn:
# 1. Read all the contents of line
# 2. Read n number of characters by using the parameter

file = open('/home/nayana/PycharmProjects/MyTestProject/test.txt')

# print(file.read())  # Reading all the contents of file
# print(file.read(11)) # Reading first 10 characters of the file

# Reading contents line by line
# print(file.readline()) # Reading first line --- Hello
# print(file.readline()) # Reading second line --- World


# Print all the contents of file line by line by using printline method
# linetext = file.readline()

#while linetext != "":
   # print(linetext)
  #  linetext = file.readline()


# readlines() method read and stores text in the list
# textline = [Hello, World, ABC, Python, Selenium, XYS]
for textline1 in file.readlines():
    print(textline1)

file.close()