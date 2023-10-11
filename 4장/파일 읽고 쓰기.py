'''

f=open("새파일.txt",'w') #파일 객체 = open(파일 이름, 파일 열기 모드) 꼴로 파일 생성 가능, 'r'은 읽기모드, 'w'는 쓰기모드, 'a'는 추가모드
f.close()


f=open("새파일.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n" %i
    f.write(data) #write를 이용해 텍스트 파일에 내용을 옮겨적음
f.close()

f=open("새파일.txt",'r') #읽기모드
line=f.readline() #readline 함수를 이용해 첫번째 줄이 화면에 출력
print(line)
f.close()

f=open("새파일.txt",'r')
while True:
    line=f.readline()
    if not line: break #더이상 읽을 줄이 없으면 break
    print(line)
f.close()

f=open("새파일.txt",'r')
lines=f.readlines() #readlines 함수를 이용해 파일 각각의 줄을 요소로 갖는 리스트로 만들어줌
for line in lines:
    print(line)
f.close()

f=open("새파일.txt",'r')
data=f.read() #read함수를 이용해 파일 내용 전체를 문자열로 돌려줌
print(data)
f.close()

f=open("새파일.txt",'a') #쓰기 모드로 이미 존재하는 파일을 열면 초기화가 되지만, 추가모드로 열면 유지한 채 추가 가능
for i in range(11,20):
    data="%d 번째 줄입니다.\n" %i
    f.write(data)
f.close()

f=open('foo.txt','w')
f.write("Life is too short, you need python")
f.close()

with open('foo.txt','w') as f: #with 문을 이용하면 파일을 매번 close할 필요가 없다
    f.write("Life is too short, you need python")

'''




