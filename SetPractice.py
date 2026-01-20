my_set = {2,3,4}
print(type(my_set))

rohan = set()
print(type(rohan))


"""
union se sirf value sath me show hoti h,
or update se value update hojaati h jaise ki s2 ki value s1 me update hojati h
"""
s = {1,2,5,6}
s2= {3,6,7}

print(s.union(s2)) # S or S2 ki value sath me aajyegi
print(s, s2) # value sath me toh hogi lekin section alag alag hojayenge
s.update(s2) # S ke ander S2 ki value update hojayegi


"""
A = {1,3,5,7,9} = String 1st
B = {2,3,5,6,8} = string 2nd
C = {2,5      } = string 3rd
Intersection = Two strings ki common values 3rd string me shows hoti hai
Intersection_update = kisi particular string ki value update krne liye use hota hai
Symmetric_difference = Two strings ki value 3rd string me update hogi lekin common values update nhi hogi
Disjoint = Dono Strings ki common values toh hai ya nhi (True or False)
Issuperset = String 2nd ki value 1st string me hai ya nhi? (True or False)
Issubset = String3rd mein jo bhi value h vo string2 me se he nikali h, isliye string3 issubst of string2 

"""

cities = {"udaipur", "vadodara","ahmedabad", "vrindavan"}
cities2 = {"vadodara", "udaipur","kota","rajkot"}
cities3 = {"vadodara", "udaipur", "ahmedabad"}


# cities3 = cities.intersection(cities2) #common cities show hogi cities 3 mein/ common cities only available between cities or cities2
# # cities3 = cities.intersection_update(cities2) # update in only cities string / common cities update hojayegi cities mein, upper jaise cities show krne ke liye cities3 bana na pad rha tha isme cities ke ander he update hojayega
# print(cities3)

# cities3 = cities.symmetric_difference(cities2) #update in cities3 strring but not common things update
# print(cities3)

# print(cities.isdisjoint(cities2)) #both have different element
# print(cities.issuperset(cities2)) #cities2 mention in cities or not?

# print(cities3.issubset(cities))
# cities.add("baroda")#cities3 mein jo bhi city h vo cities2 me se he nikali h isliye cities3 issubst of cities2 

# cities.update(cities2)
# print(cities)
# cities.remove("udaipur")
# print(cities)

# popping = cities.pop() #koi bhi random sirf ek value pop / print hojayegi 
# print(cities)
# print(popping)
# print(cities2)

# del cities #delete hojayegi cities sab:
# print(cities)
 