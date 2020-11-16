A = {9,28,38,40,56,65,78,82}
B = {13,21,33,38,45}
a = list(A)
b = list(B)
c = a + b
for i in range(len(c)-1):
    if c(i)>c(i+1):
        c(i+1),c(i) = c(i),c(i+1)
print(c)
