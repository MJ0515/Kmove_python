import random
strike = 0
ball = 0
number = 0
baseball = sorted(random.sample(range(1,10),3))
print(baseball)


while strike!=3:
    strike = 0
    ball = 0

    i = list(input("3자리숫자를 입력하세요 : "))
    print(i)
    for a in range(3):
        if int(i[a]) in baseball and int(i[a]) == baseball[0] :
            strike +=1
        elif int(i[a]) in baseball and int(i[a]) != baseball[0] :
            ball +=1   
        else:
            pass




    number+=1    
    print("스트라이크 : %d개, 볼 : %d개"%(strike,ball))

print("%d번만에 정답을 맞췄습니다."%number)
