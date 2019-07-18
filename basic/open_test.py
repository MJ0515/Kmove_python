'''
f = open('basic/test.txt','w',encoding='utf8')#class에 설정된 순서대로 적으면 명령어를 안적어줘도 된다.

for i in range(1,11):
    data = '%d번째 줄입니다.\n'%i
    f.write(data)
    
f.close

'''
'''
f=open('basic/test.txt','r',encoding='utf8')
#line = f.readline().replace('\n','')
line = f.readlines()

print(line,end='')
print(type(line))

for i in range(10):
    line[i]=line[i].replace('\n','')  #\n없애는 과정

#for i in line:
#   print(i.replace('\n','')) #\n없애는 과정 2

data = f.read()
print(data)

#print(line,end='')    
f.close()
'''
f=open('basic/test.txt','a',encoding='utf8')
for i in range(11,20):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
f.close()