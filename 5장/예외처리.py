'''

#try except 문을 이용해 예외처리하기

try:
    4/0 
except ZeroDivisionError as e: #오류 메세지를 알고 싶을때 이런 형태로 사용
    print(e)
    
try:
    a=[1,2]
    print(a[3]) #먼저 인덱싱 오류가 나기 때문에 4/0은 무시된다
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")

try:
    a=[1,2]
    print(a[3]) 
    4/0
except ZeroDivisionError as e: #이런 식으로도 불러올 수 있다
    print(e)
except IndexError as e:
    print(e)

try:
    a=[1,2]
    print(a[3])
    4/0
except(ZeroDivisionError,IndexError) as e: #합칠 수 도 있음
    print(e)    

try:
    f=open("나없는 파일",'r')
except FileNotFoundError: #pass를 이용해 회피 가능
    pass

class Bird:
    def fly(self):
        raise NotImplementedError #raise를 이용해 강제로 오류나게 가능
    
class Eagle(Bird): #상속받는 자식 클래스는 반드시 fly함수를 구현해야 한다는 의지를 raise를 통해 표출함
    pass

eagle=Eagle()
eagle.fly() #fly를 구현하지 않았기 때문에 오류 발생
    
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast") #지정해주면 정상적으로 실행이 됨

eagle=Eagle()
eagle.fly()

class MyError(Exception): #python에 내장된 Exception 클래스를 상속하면 예외를 직접 만들 수 있다
    pass

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")

class MyError(Exception):
    pass

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e: #이런식으로 적으면 오류가 뜨므로 오류 클래스에 위와 같은 __str__ 메서드를 구현해야함
    print(e)

'''

