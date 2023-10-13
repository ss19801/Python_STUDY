'''
import sys #sys함수는 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
print(sys.argv)

sys.exit() #강제로 스크립트 종료
print(sys.path) #파이썬 모듈이 저장되어 있는 경로를 반환해줌
sys.path.append("C:\\Python\\JumpToPy\\5장") #append 를 이용해 경로 이름을 추가 가능


import pickle
f=open('test.txt','wb')
data={1:'python',2:'you need'}
pickle.dump(data,f) #pickle에 내장된 dumb 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장 가능
f.close()

import pickle
f=open('test.txt','rb')
data=pickle.load(f) #load를 이용해 data의 상태를 그대로 반환함. 저장한 파일을 그대로 가져오는 것
print(data)
f.close()

import os
print(os.environ) #시스템의 환경변수를 반환함
print(os.environ['PATH'])#PATH 환경변수 내용 반환
os.chdir("C:\WINDOWS") #현재 디렉터리 위치를 바꿀 수 있음
os.getcwd() #현재 자신의 디렉토리 위치를 반환
os.system("dir") #시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출 할 때 씀
f=os.popen("dir") #시스템 명령어를 실행한 결괏값을 읽기모드의 파일 객체로 돌려줌
print(f.read()) #객체내용 보기 위해 하는거
#os.mkdir_>디렉터리 생성 os.rmdir->디렉터리 삭제(텅 비어있어야 함) os.unlink->파일을 지움 os.rename(src,dst)->src라는 이름을 dst로 바꿈

import shutil
shutil.copy('src.text','dst.txt') #shutil을 이용해 파일을 복사함. src 파일을 dst로 복사함. 

import glob
glob.glob('C:\\Python\\JumpToPy\\5장/as') #glob을 이용해 해당 위치에 있는 as로 시작하는 파일을 알려줌

import tempfile 
filename=tempfile.mkstemp() #중복되지 않는 임시 파일의 이름을 무작위로 만들어 반환해줌
print(filename)
f=tempfile.TemporaryFile() #임시 저장 공간으로 사용될 파일 객체를 돌려줌. 'wb'로 기본적으로 열리고 close를 호출하면 자동으로 사라짐
f.close()

import time
print(time.time()) #UTC를 사용해 현재 시간을 실수 형태로 반환
print(time.localtime(time.time())) #실수값을 사용해 연도,월,일,시,분,초 의 형태로 반환
print(time.asctime(time.localtime(time.time()))) #localtime으로 반환된 튜플 형태의 값을 인수로 받아 알아보기 쉬운 형태로 반환
print(time.ctime()) #위의 함수를 간단히 표시 가능, 하지만 현재시간만 반환
print(time.strftime('%x',time.localtime(time.time())))
for i in range(10):
    print(i)
    time.sleep(1)

import calendar
print(calendar.calendar(2015)) #그 해의 달력을 출력
calendar.prcal(2015) #위와 동일
calendar.prmonth(2015,12) #2015년의 12월만 보여줌 
print(calendar.weekday(2015,12,31)) #해당 날짜의 요일을 반환함, 3이 출력되는데 목요일임
print(calendar.monthrange(2015,12)) #2015년의 12월의 1일은 무엇인지와 며칠까지 있는지 알려줌

import random
print(random.random())
print(random.randint(1,55)) #1,55사이의 정수중 무작위 숫자 불러옴 

def random_pop(data):
    number=random.randint(0,len(data)-1) #인덱스
    return data.pop(number) #데이터를 pop 

if __name__=="__main__":
    data=[1,2,3,4,5]
    while data: print(random_pop(data))

def random_pop2(data):
    number=random.choice(data) #choice함수를 이용해 위와 똑같은 결과 도출
    data.remove(number)
    return number

if __name__=="__main__":
    data=[1,2,3,4,5]
    while data: print(random_pop(data))

data=[1,2,3,4,5]
random.shuffle(data) #shuffle을 이용해 섞을 수 있다
print(data)

import webbrowser
webbrowser.open("http://google.com") #웹사이트 열어줌
webbrowser.open_new("http://google.com")

#thread를 이용해 한 프로세스 안에서 2가지 이상의 일을 동시에 수행 가능

import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)
print("Start")

threads=[]
for i in range(5):
    t=threading.Thread(target=long_task) #thread를 생성
    threads.append(t)
for t in threads:
    t.start() #thread를 실행
for t in threads: #이게 없으면 End도 같이 출력 된 후 스레드의 결과가 출력
    t.join() #join으로 thread가 종료될 떄 까지 기다림

print("End")

'''






