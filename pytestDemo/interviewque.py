#1 list vs tuple
import asyncio
import time

ablist = [2,8,10,"mk"]
ablist[2] = 29
ablist.append(9)
ablist.pop(1)
print(ablist)


abtup = (4,9,"mj")
#abtup[0] = 7
print(abtup)

#2 inheritance and super

class Parent():
    def greet(self):
        return "Hello From parent"

class child(Parent):
    def __init__(self,title):
        self.title = title
    def yo(self):

        return super().greet()

obj = child("YOYo")
obj.greet()
obj.yo()

#how to create list of dict
list = [{"name":"Minakshi","age":25},
        {"name":"Vaibhav","age":27}]
print (list[1]["name"])

#lambda function
def add(x,y):
    print(x+y)

add = lambda x,y : x+y

#map is useed to modify all values in list to new logic
no = [2,7,9]
print(no[::-1])
new_list = map(lambda x : x*2,no)

filter(lambda x :x% 2 == 0,no)

#how to sort list
num =[3,1,8]
print(sorted(num))


#synchronoius : executing line by line
#asychronious : multiple task simaltionusly

def task(name):
    print(f"Start {name}")
    time.sleep(2)
    print(f"Finished {name}")
task("Minakshi")
task("Khamkar")

async def tasks(name):
    print(f"Start {name}")
    await asyncio.sleep(2)
    print(f"Finished {name}")

async def main():
    await asyncio.gather(tasks("Minakshi"),tasks("Khamkar") )

asyncio.run(main())

#@classmethod and instancemethod

class Myclass():

    @classmethod
    def classmethod(cls):
        print("Heyyyy")

    def instancemeth(self):
        print("NOOOOOOOO")

obj= Myclass()
obj.instancemeth()
Myclass.classmethod()


try:
    with open("abc.txt","r") as f:
        obj = f.read()
        print(obj)
except FileNotFoundError as e:
    print(e)

finally:
    print("It will print anyway")










