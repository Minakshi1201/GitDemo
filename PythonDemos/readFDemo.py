file = open("test.txt")
#print(file.read()) #read all contain of file
#print(file.read(2)) #read 2character of file
print(file.readline()) #read signle line at time
for line in file.readlines(): #print line by line if there is many lineas
    print(line)
file.close()

#we can open files without using close
with open("test.txt", "r") as reader:
    content = reader.readlines()
    content.reverse()
    print(content)
