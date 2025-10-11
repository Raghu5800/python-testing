file = open('/Users/raghu/Python_Projects/PythonTesting/.venv/test.txt') # can write file name if it is in the same folder test.txt
#print(file.read()) #reads the file - all content
#print(file.read(10)) # reads 2 byts / characters of the content 1st one && when reading it takes 1 place when navigating to next line

# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)

line = file.readline()
while line !="":
    print(line)
    line = file.readline()

file.close()
