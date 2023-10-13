"""
print(abs(-3)) #절대값 반환 함수

print(all([1,2,3])) #all함수는 반복가능한 자료형(리스트,문자열,튜플,딕셔너리 등)을 입력 받으며 하나라도 거짓이 있으면 False를 반환환
print(all([1,2,3,0]))

print(any([1,2,3,0])) #all과 반대로 하나라도 참이면 True를 반환환

print(chr(97)) #아스키코드를 입력받아 코드에 해당하는 문자 출력

print(dir([1,2,3])) #dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다

print(divmod(7,3)) #divmod는 2개의 숫자를 입력으로 받아 나눈 몫과 나머지를 튜플로 반환한다

for i, name in enumerate(['body','foo','bar']): #enumerate는 순서가 있는 자료형(리스트,튜플,문자열)을 입력으로 받아 인덱스값을 포함하는 enumerate 객체를 돌려주는데, for문을 이용하면 인덱스 값을 알기 쉽다
    print(i,name)

print(eval('1+2')) #eval함수는 실행가능한 문자열을 입력으로 받아 결과를 보여주는 함수, 일반적으로 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행할 때 사용
print(eval('divmod(4,3)'))

def positive(l):
    result=[]
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))

def positive(x):
    return x>0 

print(list(filter(positive,[1,-3,2,0,-5,6]))) 

print(list(filter(lambda x: x>0,[1,-3,2,0,-5,6]))) #filter와 lamda를 이용하면 변환값이 참인 것만 걸러준다

print(hex(234)) #16진수 반환 함수

a=3
print(id(a)) #id함수는 객체의 레퍼런스 값을 반환하는 함수

a=input("Enter : ") #input 함수를 이용해 입력을 받음
print(a)

print(int(3.4)) #int형으로 바꿔줌
print(int('11',2)) #int(문자열,radix) 꼴로 실행하면 radix진수로 표현된 문자열 x를 반환함
print(int('1A',16)) 

class Person: pass

a=Person()
print(isinstance(a,Person)) #isinstance 함수는 입력으로 받은 인스턴스가 클래스의 인스턴스인지 판단함.
b=3
print(isinstance(b,Person)) #클래스의 인스턴스가 아니므로 false

print(len('python')) 
print(len((1,'a'))) #len을 이용해 길이(요소의 전체개수)를 반환함

print(list('python')) #list를 이용해 입력받은 반복 가능한 자료형을 리스트로 만들어줌
a=[1,2,3]
b=list(a) #이런식으로 입력하면 리스트가 b로 들어감
print(b)

def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result
result=two_times([1,2,3,4])
print(result)

def two_times(x): return x*2
print(list(map(two_times,[1,2,3,4]))) #map함수를 이용하면 함수의 결과값이 들어감
print(list(map(lambda a: a*2,[1,2,3,4]))) #lambda를 이용해 간소화

print(max(1,2,3)) #max와 min을 이용해 최대 최소 값 반환(문자열도 가능)
print(max('python'))
print(min(1,2,3))
print(min('python'))

print(oct(34)) #8진수로 문자 반환

f=open("binary_file",'rb') #w->쓰기 모드, r->읽기모드, a->추가모드, b-> 바이너리 모드
fread2=open('read_mode.txt') #비우면 읽기모드와 똑같음

print(ord('a')) #ascii코드 값을 반환
 
print(pow(2,4)) #제곱수 함수

print(list(range(5)))
print(list(range(5,10)))
print(list(range(0,-10,-1))) #시작, 끝, 숫자사이의 거리를 뜻함

print(round(5.678,2)) #round를 이용해 반올림 가능, 뒤의 숫자는 소숫점 자리

print(sorted([3,1,2])) #sorted를 이용해 값을 정렬한 후 반환 가능, sort함수는 리스트 객체를 정렬할 뿐 반환하진 않는다
print(sorted("zero"))

print(str(3))
print(str('hi'.upper())) #str을 이용해 문자열로 반환

print(sum((1,2,3))) #sum 함수를 이용해 요소의 합을 반환

print(tuple([1,2,3])) #tuple로 반환

print(type([])) #type함수는 무슨 자료형인지 반환

print(list(zip([1,2,3],[4,5,6]))) #zip함수를 이용해 동일한 개수로 이루어진 자료형을 묶어줌
print(list(zip('abc','def'))) #[('a','d'),('b','e'),('c','f')]로 묶어줌

"""













