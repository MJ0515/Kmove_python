for i in range(2,10):
    for j in range(1, 10):
        print("%dx%d=%2d"%(i,j,i*j), end=" ")
    print('')

#방향전환
for i in range(1,10):#고정하는수(곱)
    for j in range(2, 10):#변하는수(단)
        print("%dx%d=%2d"%(j,i,i*j), end=" ")
                    #자리를 확보해준다 두자리
    print('')#줄바꾸기 ''없을떄는 \n이 나간다.