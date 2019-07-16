score = int(input("점수를입력하세요\n"))
print('입력한 점수는 %d 입니다'%score)
if score > 90:
    level = 'A'
    print("A")
elif score > 70:
    level = 'B'
    print("B")
elif score > 50:
    level = 'C'
    print("C")
elif score > 30:
    level = 'D'
    print("D")
else:
    level = 'F'
    print("F")
print('입력한 점수는 %d 입니다. 당신의 학점은 %s입니다.'%(score,level))
#format으로 문자 또는 숫자 삽입하기
print('당신의 스코어는 {}입니다.'.format(level))
print('당신의 스코어는 {}입니다.'.format('미정'))
print('당신의 스코어는 {}입니다.'.format(100))
#format으로 다양한 변수형
print('가나다라마바{}사아자차{}카'.format('빠',100))