# """
# hey here we ask a user for any table
# """
table = int(input("Ask me any table"))

for i in range (1, 13):
    if(i==11):
        break
    print(table, "X", i , "=", table*i)
