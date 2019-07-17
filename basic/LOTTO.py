#1-45사이의 번호 6개를 추출
#총 다섯번에 걸쳐 번호를 추출 정렬하여 출력
#random함수, rnadint 이용
#sorted()내장함수이용
import random #외장함수이기에 선언을 해주어야한다.

for i in range(5):#0부터4까지 돌아가면 된다. 총 다섯번!
    lotto = [0,0,0,0,0,0]#내부의값과 비교하기에 미리선언하는 것이 수월하다.
    for x in range(6):#x는 인덱스의 역할을 하게 된다.
        num=0
        while(num in lotto):#기존의 list 값과 비교해서 겹치지 않을 때 숫자를 뽑는다.
            num=random.randint(1,45)#randint는 정수

        lotto[x]=num #인덱스x자리를 num값으로 바꾼다.
    print("로또: ",sorted(lotto))

for i in range(1,6):
    print("로또: ", sorted(random.sample(range(1,46),6)))

#random은 sample이라는 함수를 가진다.
#sample은 정해진 반복 범위내에서(6)중복된 수를 생성하지 않는다.