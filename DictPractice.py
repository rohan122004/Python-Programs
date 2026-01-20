#Dictionary

# Dic = {
#     "A": "Apple",
#     "R": "Rohan"
# }
# print(Dic["A"])


# rohan = {"surname" : "chauhan" , "age": 19, "father": "bhagchand ji"}
# # print(rohan["age"])
# # # print(rohan.get("age2")) #.get ki wjah se error show nhi krega only none dikhayega
# # rohan["age"] = 21
# # print(rohan["age"])

# # print(rohan.keys()) #agar me bhul gya string me kya hein, toh ye keys dikhati h strings ki 
# # print(rohan.values()) #show the value of keys


# for key, value in rohan.items():
#         print(f"The value of {key} is {value} ")


# print(rohan.items())


ep1= {1:78, 2:45, 3:90, 4:89}
ep2 = {5:88, 6:95}

ep1.update(ep2)
ep1.clear
print(ep1)