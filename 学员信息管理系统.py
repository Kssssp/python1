a=['zs','ls','ww','zl']
c=''
while True:
    q=input("请输入要执行的操作:")
    c==int(q)
    if c==1:
        name1 = input('请输入要添加的姓名：')
        a.append(name1)
        
    elif c==2:
        i = input('请输入学员序号：')
        name2 = input('请输入修改后的姓名：')
        a.replace(a[i],name2)
        
    elif c==3:
        b = input('请输入要查询的序号')
        print(a[b])
        if b==211:
            for j in range(len(a)):
                print(a[j],j)
    elif c==4:
        d1 = input('请输入要删除的学员序号：')
        a.remove(d1)
    elif c==0:
        break

        
        
