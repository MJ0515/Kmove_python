import re #정규표현식
custlist=[] #고객의 전체정보를 리스트로 관리
page=-1 #현재 데이터가 몇건 있는지 체크(인덱스값으로)

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

    if choice=="I":
        print("고객 정보 입력")
        name = input("이름을입력하세요")
        
        sex = input("성별을입력하세요")
        while sex not in ('M', 'm', 'F', 'f'):
            sex = input("오류입니다. 성별을입력하세요")
        sex = sex.upper()
        
        email = input("email을입력하세요")
        p = re.compile('@')
        e = p.search(email)
        while e == None:
            email = input("@를 포함하여 email을입력하세요")
            p = re.compile('@')
            
            e = p.search(email)

        #p= re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
        #while True:
            #costomer['email']=input("이메일을 입력하세요:")
             #e = p.search(customer['email'])
             #if e:
                #break
             #else:
                #print('@를 포함한 정확한 이메일을 써주세요')

        #check = 0
        #for i in custlist:
            #if i['email']==customer['email']:
                #check = 1
        #if check == 0:
            #break
        #print("중복되는 이메일이 있음")
        print(email)    

        birth = input("출생년도를 입력하세요")
        while len(birth) != 4:
            birth = input("출생년도를 4자리로 입력하세요")
        print(birth)
            
        customer={'name':name,'sex': sex,"email": email,"birthyear":birth}

        custlist.append(customer)
        print(custlist)

        '''
        customer={'name':'','sex': '',"email":'',"birthyear":''}
        customer['name']=input("이름을 입력하세요: ")
        while True:
            customer['sex']=input("성별입력하세요").upper()
            if customer['sex'] in ('M','F'):
                break
            else:
                print("다시입력하세요")

        '''

    elif choice=="C":
        print("현재 고객 정보 조회")
        page
    elif choice == 'P':
        print("이전 고객 정보 조회")
    elif choice == 'N':
        print("다음 고객 정보 조회")
    elif choice=='D':
        print("고객 정보 삭제")
    elif choice=="U": 
        print("고객 정보 수정")
    elif choice=="Q":
        print("프로그램 종료")
        break
    else:
        print("잘못입력하셨습니다.")
