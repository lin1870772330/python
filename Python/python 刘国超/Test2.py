a = 1
b = 1
c = 2
s = a+b+c
print(a,b,c, end=''" ")
for i in range(5):
    a = b+c
    b = a+c
    c = a+b
    s = a+b+c
    print(a,b,c,end=''" ")
a = b+c
b = a + c
print(a,b)
s = a+ b+ s
print(s)
