#List is contain diffent data types and its editable
values = [2,6,"xyz",8.5,7]
print(values[0]) #print first index of list
print(values[-1]) #print last index
print(values[1:4]) #print from source to destination index

#To insert new value in  between list you can use insert
values.insert(3,"abc")
print(values)

#to add new value at the end of list you can use append
values.append("End")
print(values)

#update value
values[2] ="MNO"
print(values)

#delete particular index
del values[1]
print(values)

##
#tuple is as same as list but its immutable
val =(1,3,"XYZ",6)
print(val[1])
#val[2] ="xyz" #not support item assignment

#Dictionary contain data on key-values format

dic = {4:"ABC",6:"60","5":"Hello"} #here 4 is key and abc is value
#you can print data by key
print(dic[6])

#create empty dictory and we can add values to it live

dict = {}
dict["FirstName"] = "Minakshi"
dict["LastName"] = "Khamkar"
dict["Age"] = 25
print(dict)

print(dict.get("FirstName")) #print elemnet by using get

#adding new element to dict

dict["Gender"]= "Female"
#updating exsiting element
dict["Gender"] = "Male"
print(dict)

#removing an element from dict
del dict["FirstName"] #removing an item by key
print(dict)
dict.pop("Age")#remove key and return value
print(dict)
#dict.clear() #empty whole dict

#Iterating through dictionary
d ={1:"ABC",2:"XYZ",3:"MNO"}
for key in d:
    print(key) # only print key
for value in d.values():
     print(value)   #only print value
for key,value in d.items():
    print(f"{key}:{value}") #print both key and value





#