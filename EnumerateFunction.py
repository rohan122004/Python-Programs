marks = [23, 45, 56, 67, 9, 1, 5]


##without enumerate function 
#index = 0
# for mark in marks:
#     print (mark)
#     if (index == 3):
#         print("HELLO WORLD")
#     index +=1


##with enumerate function
for index, mark in enumerate(marks, start =1):
    print (mark)
    if (index == 3):
        print("HELLO WORLD")
    