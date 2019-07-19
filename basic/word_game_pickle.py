import random
import time
import pickle

count = 0
x = 0
word = [ '가구', '나비', '다람쥐', '로봇', '마술', '바지', '사슴']

rank={}
def sortV(x):#(k,v)
    return x[1]#v값으로 return 됨 

while True:
    print("1. 문제불러오기 2.문제저장 3.타자게임 4. 등수확인 5.저장하기 6.불러오기")
    menu = input("메뉴를 선택하세요\n")
    
    if menu=='1':

        f=open('basic/word.txt','rb')
        word=word+pickle.load(f)
        f.close()
        print(word)

    elif menu=='2':
        f=open('basic/word.txt','wb')  
        pickle.dump(word,f)
        f.close()  

    elif menu == '3':
        input("게임을 시작하려면 엔터를 누르세요")
        start = time.time()
        count = 0

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

        print("틀린개수: %d 걸린시간: %.2f"%(x,t)) #pirnt('걸린시간 : {:.0f}초'.format(t))
        name = input("사용자의 이름을 입력하세요")
        rank[name] = float(t)

    elif menu=='4':
        ranklist = sorted(rank.items(),key=sortV)#시간으로 정렬하기위함
        num = 1
        for k,v in ranklist:
            print("%d등 %s %d"%(num,k,v))
            num = num+1

    elif menu == '5':
        f = open('rank.txt','w',encoding = 'utf8')
        text = ''
        items=rank.items()
        for k,v in items:        
            text=text+k+':'+str(v)+'\n'
        f.writelines(text)
        f.close()

    elif menu=='6':
        f=open('rank.txt','r',encoding = 'utf8')
        line = 1
        while line:
            line = f.readline().replace("\n","")
            if not(line==''):
                k,v = line.split(':')
                rank[k]=float(v)



    else:
        print("메뉴를 잘못입력하셨습니다.")
        
        
        
