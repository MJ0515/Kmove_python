import random
import time

count = 0
x = 0
word = [ '가구', '나비', '다람쥐', '로봇', '마술', '바지', '사슴']

input("게임을 시작하려면 엔터를 누르세요")
start = time.time()
Q = random.choice(word)
while count <= 4:

    
    print("#문제",count+1)
    print(Q)
    
    A = input("정답을입력하세요. ")
    
    if Q==A:
        print("정답")
        count+=1
        Q = random.choice(word)

    else:
        print("오답")
        x +=1

finish = time.time()
t= finish-start

print("틀린개수: %d 걸린시간: %.0f"%(x,t)) #pirnt('걸린시간 : {:.0f}초'.format(t))
name = input("사용자의 이름을 입력하세요")
