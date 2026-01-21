"""
This program shows how else works with loops in python.
"""
##LOOP-ELSE

for i in range(5):
    print(i)
    if i==4:
        print("yes")
        break #break use krne se else print nhi hoga kyuki for loop khatam krdiya h
else:
    print("Number not found")


## WHILE-ELSE

i = 0
while i<7:
    print(i)
    i = i+1
    if i==5:
        break #agar me if or break use kru toh else print nhi hoga or loop khtam hojayega,
else: print("Loop completed without break")