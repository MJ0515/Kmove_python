import re
import pickle
import os
custlist=[]
page=-1

def exe(choice):
        if choice=='I':
            insertData()
        
        elif choice=='C':
            page = curSearch(page)#globa안쓰는 경우
        
        elif choice=='P':
            preSearch()#global 쓰는경우

        elif choice=='N':
            nextSearch()

        elif choice=='U':
            updateData()
        
        elif choice=='D':
            deleteData()
        
        elif choice=='Q':
            Quit()
            
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


def insertData():
    print("고객 정보 입력")
    customer={'name':'','sex': '',"email":'',"birthyear":''}
    customer['name']=input("이름을 입력하세요: ")
    while True:
        customer['sex']=input("성별입력하세요").upper()
        if customer['sex'] in ('M','F'):
            break
        else:
            print("다시입력하세요")
    while True:    
        p= re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')#중괄호는 몇자리 적을건지 {4,10}은 4자리부터 10자리까지
        while True:
            customer['email']=input("이메일을 입력하세요:")
            e = p.search(customer['email'])
            if e:
                break
            else:
                print('@를 포함한 정확한 이메일을 써주세요')

        check = 0
        for i in custlist:
            if i['email']==customer['email']:
                check = 1
        if check == 0:
            break
        print("중복되는 이메일이 있음")

    while True:
            customer['birthyear']= input("출생년도4자리를 입력하세요")

            if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
                break
    custlist.append(customer)
    print(custlist)

    page = len(custlist)-1
    print(page)

def curSearch(page):
    global page
    print("현재 고객 정보 조회")
    if page >=0:
        print(custlist[page])
    else:
        print("입력된정보가없습니다")
    return page

def preSearch():
    print("이전 고객 정보 조회")
    global page
    if page<=0 :
        print("첫번째페이지이므로 이전페이지 이동이 불가합니다.")
    else:
        print(custlist[page-1])

def nextSearch():
    global page
    print("다음 고객 정보 조회")
    if page >= len(custlist)-1  :
        print("다음데이터가없습니다.")
    else:
        print(custlist[page+1])

def updateData():
    global page
    print("고객 정보 삭제")
    #유일값인 이메일로 찾는다
    print(custlist)
    delet=input("지우고싶은 정보의 이메일을 입력하세요")
    delok = 0
    for i in range(0,len(custlist)):
        if custlist[i]['email'] == delet:
            print('{}고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            print(custlist)
            delok = 1
            break
        
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
            print(custlist)

def deleteData():
    while True:
        choicel = input('수정하려는 이메일을 입력하세요')
        idx=-1
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choicel:
                idx = i
                break

        if idx == -1:
            print('등록되지안흔 이메일입니다.')
            break

        choice2=input('''
        다음중 수정할 정보를 골라주세요
                name, sex, birthyear
        (수정할 정보가 없으면 exit 입력)
        ''')

        if choice2 in ('name','sex','birthyear'):
            custlist[idx][choice2]=input('수정할{}를 입력하세요 : '.format(choice2))
            break
        elif choice2 == 'exit':
            break
        else:
            print('존재하지 않는 정보입니다.')
            break

def Quit():
    print("프로그램 종료")
    
    return

def loadData():
    #파일크기가 0보다 클 경우에 읽어옴
    #if os.path.getsize('basic/data.pkl')>0:
    #파일이 존재할 경우에 읽어옴

    global page
    if os.path.exists("basic/data.pkl"):
        with open('basic/data.pkl','rd')as f:
            custlist = pickle.load(f)
            page = len((custlist)-1)

   