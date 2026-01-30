#jab program chal raha hota hai aur beech me koi galti (error) aa jaati hai, us galti ko Python me Exception kehte hain.
"""
Example:
print(10 / 0)
Isme 10 ko 0 se divide kar rahe ho
Ye galat hai
Program turant ruk jaayega
"""


#Exception Handling matlab: Error aane par bhi program ko control me rakhna Crash hone ke bajay, proper message dena


a =  (input("Enter number"))
print(f"multiplication table of {a} is:")
try:
    for i in range (1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("okbye")


#----------------
##finally keyword



def func1():
    try:
        l = [6, 3, 5, 6]
        i = int(input("Enter number"))
        print(l[i])
        return 1
    except :
        print("error occured")
        return "no"
    finally:
        print("i am always executed")
x = func1()
print(x)



#---------------------------
#Raise Keyword
a = int(input("Enter a number between 5 to 9"))

if (a < 5 or a > 9):
    raise ValueError ("a number between 5 to 10")
print("Enter a valid number")