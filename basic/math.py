#eval() 문자열로 되어있는걸 실제 진행해준다. 연산자를 따로 비교하지않아도된다.

import random
import time

math = ['+','-','*','/'] #//로 나누기를 사용하면 int처리하지 않아도된다.
count=0

input("문제를 시작하려면 엔터를 누르세요.")
start = time.time()

for i in range(5):
    a = random.randint(1,100)
    b = random.randint(1,100)
    m = math[random.randint(0,3)] #m=random.choice(math)
    
    print('%d%s%d = ' %(a,m,b)) #문제 출제

    Q = ('%d%s%d' %(a,m,b)) # Q = str(a)+m+str(b)  
    A = int(input())

    
    if A == eval(Q):
        print("정답!")
        count+=1 #count=count+1
    else:
        print("오답!")

finish = time.time() 
Time = finish-start  

print("%d개맞음" %count)
print("걸린시간 : %dsec"%(Time)) #print("걸린시간 : %.0f초"%(Time))   
    
