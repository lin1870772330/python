a = [1,3,5,9,11,13]
b = int(input("请输入一个数："))
c = a+b
for i in range(0,len(c)-1):
    for j in range(0,len(c)-i-1):
        if c[j]>c[j+1]:
            c[j+1],c[j]=c[j],c[j+1]
print(c)



