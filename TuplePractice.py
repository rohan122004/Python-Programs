#Tuples are immutable


# tup = (2,43,12,54)
# print(type(tup), tup)


## can we modify a tuple? 
"""
if we want to change tuple 
first we have to convert tuple into list
and then after changing in list then again convert
list into tuple, using this method tuple canbe modified indirectly
"""

countries = ("india", "india", "australia", "finland", "pakisthan", 2, 4, 6, 6, 6, 8, 9,)
print(type(countries))

# t = list(countries)  #converting tup into list
# t.append("Russia") #add russia in the end
# t.pop(3) #delete 3rd indexing or countries 
# t[2] = "Japan" #replacing index 2 to japan
# countries = tuple(t)
# print(countries)

# cou = countries.count("india")
# print("india is repeating",cou,"times")



##find index of value 6 between index 4 and 10
res = countries.index(6, 4, 10) # it is using particular value indexing like 6value  is on 7 indexing but i want 8th indexing 6 value so i do i want 8 to 10 indexing in that i want 6 value
print(res)


