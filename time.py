#input함수를 활용한다.
import time

input("시작하시려면 엔터를 누르세요.")
start = time.time()
input("20초 후에 다시 엔터를 누릅니다.")
finish = time.time()

result = int(finish-start)

print("실제시간 : %d 초" %(result))
print("차이 : %d 초"%abs(20-result))#양수만 반환하도록한다.