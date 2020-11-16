A=[9,28,38,40,56,65,78,82]
B=[13,21,33,38,45]
C=A+B
for i in range(len(C)-1):
    for j in range(i,i+1):
        if C[j] >C[j+1]:
            C[j+1],C[j]=C[j],C[j+1]
print(C)
