#if statment
a = 6
if a > 10:
    print("Condition is not correct")
else:
    print("Condition is  correct")
print("It will print")

#Loop Statement
obj = [2,3,5,8]
for i in obj:
    print(i *2)

#print sum of first 5 numbers
a =0
for i in range(1,6): #iterate from 1 to 5
    a = a+i
print(a)

##
for k in range(1,10,2):
    print(k)

for m in range(10):
    print(m)

#whilw loop execute contiously until condition is not match
i =4
while i > 1:
    if i ==3:
        i = i - 1
        continue
    print(i)
    i = i - 1



