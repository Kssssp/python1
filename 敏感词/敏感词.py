f=[]
for i in open('filter.txt'):
    f.append(i.rstrip())
    
text = input('请输入一段话：')
for each in f:
    if each in text:
        text = text.replace(each, '**')
else:
    print(text)
