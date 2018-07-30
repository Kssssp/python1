a=['年龄','身高','体重','收入']
b=['最低年龄','最低身高','最低体重','最低收入','最高年龄','最高身高','最高体重','最高收入']
boy=[]
girl=[]
boy1=[]
girl1=[]
flag = 0
for i in range(4):
    print('请输入男生'+a[i],end=' ')
    boy.append(input())
print(boy)
for i in range(4):
    print('请输入女生'+a[i],end=' ')
    girl.append(input())
print(girl)

for i in range(8):
    print('请输入男生要求'+b[i],end=' ')
    boy1.append(input())
print(boy1)
for i in range(8):
    print('请输入女生要求'+b[i],end=' ')
    girl1.append(input())
print(girl1)
    
for i in range(4):
    if girl[i]>=boy1[i] and girl[i]<=boy1[i+4]:
        flag+=1
for i in range(4):
    if boy[i]>=girl1[i] and boy[i]<=girl1[i+4]:
        flag+=1

        
if flag==8:
    print('配对成功！')
else:
    print('配对失败！')
