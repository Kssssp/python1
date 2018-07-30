while True:
    
    l=input("请输入公里数：")

    while not l.isdigit():
        print("输入不合法！")
        l=input("请输入公里数：")

    k=int(l)
    if k<=0:
        print('请输入正确的公里数进行计算，程序结束')
        break
    elif k<=2:
        print(8)
    elif k>2 and k<=12:
        print(8+(k-2)*1.2)
    elif k>12:
        print(8+(k-2)*1.5)
