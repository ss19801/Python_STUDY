'''

def add(a,b):
    return a+b

a=1
b=2
c=add(a,b)
print(c)

def say(): #입력값이없다면 그냥 반환
    return "Hi"
print(say())

def add(a,b):
    print("%d,%d의 합은 %d입니다. "%(a,b,a+b)) #결괏값이 없는 함수.
a=add(3,4)
print(a) #None이 출력된다. 왜냐하면 함수가 반환하는 값이 없기 때문

def say():
    print("Hi") #결괏값, 입력값이 둘다 없으면 밑의 경우처럼 호출하면 됨
say()

def add(a,b):
    return(a+b)

result=add(a=3,b=7)
print(result) #이런식으로도 사용 가능

def add_many(*args): #*매개변수로 매개변수 부분을 바꾸면 입력값이 몇개가 되는지 몰라도 함수 정의 가능
    result=0
    for i in args:
        result+=i
    return result

result=add_many(1,2,3)
print(result)

def add_mul(choice,*args):
    if choice=='add':
        result=0
        for i in args:
            result+=i
    elif choice=='mul':
        result=1
        for i in args:
            result*=i
    return result

result=add_mul('add',1,2,3,4,5)
print(result)
result=add_mul('mul',1,2,3,4,5)
print(result)


def print_kwargs(**kwargs): #딕셔너리의 형식으로 출력
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo',age=3)

def add_and_mul(a,b):
    return a+b,a*b #결과값이 두개
result=add_and_mul(3,4) 
print(result) #두개의 결과가 아니라 하나의 튜플으로 나온다. 따라서 둘 다 나옴
result1,result2=add_and_mul(3,4) #이런식으로 선언하면 result1엔 7, result2엔 12가 들어간다

def say_nick(nick):
    if nick=='바보': return #return을 단독으로 적어 함수를 바로 빠져나갈 수 있음
    print("나의 별명은 %s입니다." %nick)
say_nick('땅미')
say_nick('바보') #바보이기 때문에 빠져나가서 print가 실행되지 않음

def say_myself(name,old,man=True): #초깃값 미리 설정하기
    print("나의 이름은 %s입니다."%name)
    print("나이는 %d살입니다."%old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

a=1
def vartest(a):
    a+=1
vartest(a) #a라는 변수에 접근을 하지 못해서 덧셈이 행해지지 않음
print(a)

a=1
def vartest(a):
    a+=1
    return a #return 을 이용해 해결 가능
a=vartest(a)
print(a)

a=1
def vartest():
    global a #global을 이용해 해결 가능. 하지만 좋은 함수는 아님
    a+=1
vartest()
print(a)

add=lambda a,b:a+b #def를 사용할 수 없거나 간결한 함수에 사용. lambda 매개변수 1,2 : 표현식 꼴
result=add(3,4) 
print(result)

'''




