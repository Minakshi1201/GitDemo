#class is ussr defined protocol it contained variable, functions, constructor etc.
#function is used inside class they called method
#class variable is static and instance variable is differ they declared inside contructor
#self keyword is mandetory to caloling variable into method

class calculator:
    num = 100 #class varible
    #default constructor created by __init__
    def __init__(self,a,b): #instance variable
        self.FirstNo = a
        self.SecondNo = b
        print("It will called automatically when object is created")

    def getData(self):
        print("Print the data")
    def summation(self):
        return self.FirstNo + self.SecondNo + calculator.num

obj = calculator(3,4)  #object crettion
obj.getData()
print(obj.summation())

obj1 = calculator(20,30)  #object crettion
obj1.getData()
print(obj1.summation())
