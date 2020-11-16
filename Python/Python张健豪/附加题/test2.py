number = int(input("请输入住户数(输入2020)："))
if 0<number<10:
    print("共：",number)
elif 10<=number<100:
    print("共：",number*2-9)
elif 100<=number<1000:
    print("共：",number*3-111)
elif 1000<=number<9999:
    print("共：",number*4-1111)