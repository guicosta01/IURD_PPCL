
a = []
list_00  = []
list_num = []
b = 0

for i in range(100):
    b += 10
    a.append(b)
    
for i in range(len(a)):
    list_00.append('000')

for i in range(len(a)):
    list_num.append(list_00[i] + str(a[i]))

for i in range(len(a)):
    print(list_num[i])


