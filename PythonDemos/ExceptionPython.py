itemcart = 0
if itemcart != 2:
    #raise Exception("Itemcart is empty")
    pass #it will retrun nothing it will prevent from error of running empty code block
assert(itemcart == 0) #if condition is false then it will raise assert error

#try and except
#try containg code for exception and except block contain exception error

try:
    with open("abc.txt") as reader:
        print(reader.read())
#except:
 #   print("There is no such file hence this statement is executed") #user defined exception

except Exception as e: #it will print error that will python thrown
    print(e)


