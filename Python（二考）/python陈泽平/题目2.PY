n=1
S=0
while 20>=n:
    if n==1:
        S=S+n
        n=n+1
    else:
        g=n*fact(n-1)#求n的阶乘
        n=n+1
        S=S+g
print(S)
