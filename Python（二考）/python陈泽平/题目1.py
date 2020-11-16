i=1
s=0
while 100>=i:
    if i%3!=0 or i%7!=0:
        s=s+i
        i=i+1
    else:
        s=s
        i=i+1
print(s)
