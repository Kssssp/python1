h = input('请输入身高：')
f = input('请输入体重：')
w = int(f)
a = int(h)-105
if w<a:
    print('偏瘦')
elif w == a:
    print('正常')
elif w>a:
    print('偏胖')
