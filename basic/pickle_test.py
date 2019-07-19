import pickle

data = {1:'python',2:'you'}

f= open('test_p.txt','wb')
pickle.dump(data,f)
#dump는 파일로 저장할때 쓴다. #dumps는 내부적으로 사용될때
f.close()

f = open('test_p.txt','rb')
data1=pickle.load(f)
f.close()
