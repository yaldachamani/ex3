n = int(input("please insert the rows : "))
m = int(input("please insert the columns : "))
array = []
array = [["#*" for j in range(m)] for i in range(n)]
for i in range(n):
    print(array[i])