print('FlipFlop游戏')# 游戏名称
print('规则当遇到3的倍数就要说“Flip”，遇到5的倍数就要说“Flop”既为3的倍数又为5的倍数则要说“FlipFlop”，说错的话表演节目或罚酒。 ：')
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
        print('FlipFlop')
        
    if i%3==0 and i%5!=0:
        print('Flip')
        print(i)
        
    if i%5==0 and i%3!=0:
        print('Flop')
        print(i)
        
    

