# Another file of opening the file
# If we use this method to open the file, we need not to write the close statement, it will automatically close the file once the reading or writing is done

# Read the file and store all the lines in list
# Reverse the list
# Write the list back to the file
with open('/home/nayana/PycharmProjects/MyTestProject/test.txt', 'r') as reader:
    fileContent = reader.readlines()
    reversed(fileContent)
    with open('/home/nayana/PycharmProjects/MyTestProject/test.txt', 'w') as writer:
        for textline in reversed(fileContent):
            writer.write(textline )

