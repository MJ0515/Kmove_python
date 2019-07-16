#while문을 이용한 리스트데이터관리 프로그램

listdata = []

while True:
    print('''
    =========================== 리스트데이터관리==============================
    1.리스트에추가  2. 리스트데이타수정  3. 리스트데이타 삭제  4. 종료
    ''')
    menu = int(input("메뉴를 선택하세요"))
    if menu == 4:
        break
    elif menu == 1:
        data = input("추가할 데이터를 입력하세요.")
        listdata.append(data)
        #리스트에 데이터를 추가
        print(listdata)
    elif menu == 2:
        print(listdata)
        dataindex = int(input("수정을 원하는 데이터의 인덱스를 입력하세요"))
    
        if len(listdata) < dataindex-1:
            print("범위에 벗어났습니다. 다시입력해주세요")
            continue
        data= input("수정하고자하는 데이터를 입력하세요")
        listdata[dataindex]=data
        print(listdata)
        #리스트에서 원하는 데이터를 수정
    elif menu == 3:
        print(listdata)
        dataindex = int(input("삭제를 원하는 데이터의 인덱스를 입력하세요"))
        del listdata[dataindex]
        print(listdata)
        #리스트에서 원하는 데이터를 삭제