# example : value_if_true condition value_if_wrong
a = 303
b = 305

print ("A") if a > b else print ("B") if b == a else print("B")


c = 9 if a > b else ("no")
print(c)
