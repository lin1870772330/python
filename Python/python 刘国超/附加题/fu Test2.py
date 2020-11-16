n = int(input("请输入班级总人数："))
y = []
for i in range(n) :
    fen = int(input("请输入分数："))
    y.append(fen)
print(max(y))
print(min(y))
print(sum(y)/n)
