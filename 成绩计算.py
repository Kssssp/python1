while True:
    
    grade=input("请输入成绩：")

    while not grade.isdigit():
        print("输入不合法！")
        grade=input("请输入成绩：")

    x=int(grade)
        
    if 60<=x and x<70:
        print('D')
    elif 70<=x and x<80:
        print('C')
    elif 80<=x and x<90:
        print('B')
    elif 90<=x and x<=100:
        print('A')
    elif 0<=x and x<60:
        print('不合格')

    else:
        print("无效成绩！")

