print("从1开始数")
print("说出你应说的数字或话")
for i in range(1,101):
    a = int(input(":"))
    if i>5 and i%3 == 0 and i%5 == 0:
        if  a%3 == 0 and a%5 == 0:
           print("你说错了，表演节目或罚酒")
    if i>2 and i%3 == 0:      
        if a>2 and a%3 == 0:
           print("你说错了，表演节目或罚酒")
    if i>4 and i%5 ==0:
        if a>4 and a%5 ==0:
            print("你说错了，表演节目或罚酒")
    



for i in range(1,101):
    if i>5 and i%3 == 0 and i%5 == 0:
        
        print("FlipPlop")
    elif i>2 and i%3 == 0:
        print("Flip")
    elif i>4 and i%5 ==0:
        print("Flop")
    
