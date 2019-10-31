# import os
# import sys
# import fileinput

textToSearch = input("Text to search for: ")
textToReplace = input("Text to replace: ")
fileToReplace = input("Enter the file path with file name: ")

# Reading the file
with open(fileToReplace, 'r') as workFile:
    fileData = workFile.read()

# Replacing the target string
fileData = fileData.replace(textToSearch, textToReplace)

# Writing the output in the file
with open(fileToReplace, 'w') as workFile:
    workFile.write(fileData)

print("Replacing {} with {} is completed in {}".format(textToSearch, textToReplace, fileToReplace))

# for line in fileinput.input(fileToReplace):
#     if textToSearch in line :
#         print ("{0} is present in the {1}".format(textToSearch, fileToReplace))
#     else:
#         print ("{0} is not present in the {1}, Please try with another file".format(textToSearch, fileToReplace))
#     tempFile.write(line.replace(textToSearch, textToReplace))
# tempFile.close()

