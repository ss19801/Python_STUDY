# %s -> 문자열, %c -> 문자 1개(Character), %d -> 정수(Integer), %f -> 부동 소수, %o -> 8진수, %x -> 16진수, %% -> 문자 %
# %s -> 어떠한 형태의 값이든 String 형으로 받아드림.

#print("Error is %d%%." % 98) # %를 하나만 쓰면 오류가 뜸.

#print("%10s" % "hi") # 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬. 나머지는 다 공백.
#print("%-10sjane" % "hi")  # 위와 반대로 이것은 왼쪽으로 정렬.

#print("%0.4f" % 3.42134234) # 뒤의 소수점 네번째 자리 까지 자르기.
#print("%10.4f" % 3.42134234) # 소수점 네번째 까지 자르고 전체 길이가 10개, 오른쪽으로 정렬.

'''
#format 함수를 사용하기.
number=10
day="three"
print("I ate {0} apples. so I was sick for {1} days.".format(number,day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10,day="three")) #똑같은 결과가 나옴.
'''

'''
#정렬하기

print("{0:<10}".format("hi")) #왼쪽 정렬
print("{0:>10}".format("hi")) #오른쪽 정렬
print("{0:^10}".format("hi")) #중앙 정렬
print("{0:=^10}".format("hi")) #기호 앞에 문자 적으면 남은 여백에 그 문자로 채워줌
'''

'''
#format 함수 소수점, 문자 표현하기

y=3.4213424
print("{0:0.4f}".format(y)) 
print("{0:10.4f}".format(y))

print("{{and}}".format()) #{}문자를 사용할려면

'''

'''
#f문자열 포매팅. 위에것과 동일하게 기능들 사용하기

name='홍길동'
age=30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')
d = {'name':'홍길동','age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.') #딕셔너리 이용하기
print(f'{"python":!^12}')
print("{0:!^12}".format('python'))
'''

'''
# 문자열 관련 함수

a="hobby"
print(a.count('b')) #문자열에서 b의 개수

a='Python is the best choice' #문자열에서 b가 처음 나오는 위치를 알려줌, 만약 찾으려고 하는 문자가 없으면 -1 반환
print(a.find('b'))

a='Life is too short' #find와 똑같은 기능, 하지만 find와 달리 찾으려고 하는 문자가 없으면 오류를 발생시킨다
print(a.index('t'))

print(",".join('abcd')) #join을 이용해 각각의 문자 사이에 ""안의 문자를 삽입함.
print(",".join(['a','b','c','d'])) #리스트나 튜플에서도 사용 가능

a='hi' 
print(a.upper()) #대문자 변환
a='HI'
print(a.lower()) #소문자 변환

a=' hi '
print(a.lstrip()) #왼쪽 공백 지우기
print(a.rstrip()) #오른쪽 공백 지우기   
print(a.strip()) #양쪽 공백 지우기

a='Life is too short'
print(a.replace("Life","Your leg")) #replace 함수를 이용해 문자열 바꿀 수 있음

a='Life is too short'
print(a.split()) #split 함수를 이용해 문자열을 나눌 수 있음. 이때 나뉜 문자들은 하나씩 리스트에 들어감.
b="a:b:c:d"
print(b.split(':')) # 괄호안의 문자를 기준으로 나눔
'''

'''
#리스트 자료형

a=[1,2,3] #리스트 초기설정
print(a) #a 전체가 출력됨 ([1,2,3])
print(a[0]) #a의 0번째 인덱스의 값 출력
print(a[0]+a[2]) #a의 0,2번째 인덱스의 값 연산 가능
print(a[-1]) #a의 -1번째 인덱스, 즉 오른쪽 첫번째 값 불러옴

a=[1,2,3,['a','b','c']] #리스트 안에 리스트 집어넣을 수 있음
print(a) 
print(a[-1]) #마지막 인덱스의 값인 ['a','b','c']를 불러옴
print(a[3]) #""
print(a[-1][0]) #마지막 인덱스 리스트에서 첫번째 인덱스의 값 즉 'a'를 끄집어 냄

a=[1,2,['a','b',['Life','is']]] #삼중 리스트
print(a[2][2][0]) #'Life' 가 출력됨. 

a=[1,2,3,4,5] 
print(a[0:2]) #list를 0부터 2까지 슬라이싱
b=a[:2] 
c=a[2:]
print(b) #0~2
print(c) #2~끝까지
print(a[1:3]) #[2,3]이 출력됨

a=[1,2,3,['a','b','c'],4,5]
print(a[2:5]) #리스트가 들어가 있어도 출력이 됨
print(a[3][:2]) #리스트 안의 2번째 값 까지 출력 -> ['a','b'] 가 출력됨

a=[1,2,3]
b=[4,5,6]
print(a+b) #list를 더해줌
print(a*3) #list를 반복하게 해줌 123123123 이런식으로 
print(len(a)) #list a 의 길이를 알랴줌

a=[1,2,3]
# print(a[2]+'hi') 는 오류가 뜸 왜냐, 리스트 안에 들어있는 값은 정수인데 hi는 문자열임. 따라서 아래로 하면 해결
print(str(a[2])+"hi")

a=[1,2,3]
a[2]=4 #리스트 값 수정
print(a)
del a[1] #1번째 인덱스 삭제
print(a)
a=[1,2,3,4,5]
del a[2:] #a의 2 인덱스 이후의 것들 모두 삭제
print(a)

a=[1,2,3]
a.append(4) #리스트의 마지막에 추가하는 함수 append
a.append([5,6]) #append를 이용해 모든 자료형 추가 가능. 여기선 리스트를 집어넣음
print(a)

a=[1,4,3,2]
a.sort() #sort를 이용하여 정렬 가능 
print(a)
a=['a','c','b'] 
a.sort() #문자도 정렬 가능
print(a)

a=['a','c','b']
a.reverse() #리스트를 역순으로 뒤집어줌
print(a)

a=[1,2,3]
print(a.index(3)) #값의 인덱스를 반환, 만약 괄호안의 값이 없다면 오류가 발생

a=[1,2,3] 
a.insert(0,4) # 0번재 인덱스에 4라는 값을 추가함. (index,value)
print(a)

a=[1,2,3,1,2,3]
a.remove(3) #첫번째로 나오는 값을 지워줌. 첫번째만.
print(a)
a.remove(3) #뒤에 3 지울려면 한번 더 실행시켜줘야함.
print(a)

a=[1,2,3]
print(a.pop()) #pop()은 맨 마지막 요소를 반환 하고 그 요소를 삭제함
print(a)
a=[1,2,3]
print(a.pop(1)) #괄호 안의 인덱스의 값을 반환하고 삭제함
print(a)

a=[1,2,3,1]
print(a.count(1)) #리스트에 1이 몇번 들어가는지 알려줌

a=[1,2,3]
a.extend([4,5]) #extend 함수를 이용하여 리스트에 리스트를 더하게 해줌. 꼭 인자에 리스트가 들어가야 함
print(a)
b=[6,7]
a.extend(b)
print(a)
a+=[8,9] #이런식으로도 사용 가능
print(a)

#튜플 자료형 -> 튜플은 리스트와 달리 값을 바꿀 수 없다
t1=(1,2,3) # 기본적인 튜플
t2(1,) #한가지 요소만 가지면 뒤에 콤마를 적어야함
t3=1,2,3 #꼭 괄호를 넣을 필요가 없음

t1=(1,2,'a','b')
print(t1[0])
print(t1[3]) #인덱스 값 불러오기

t1=(1,2,'a','b')
print(t1[1:]) #슬라이싱
t2=(3,4)
print(t1+t2) #연산가능, 합칠 수 있음
print(t2*3)
len(t1) #튜플의 길이

t1=(1,2,3) 
print(t1+(4,)) #튜플에 4라는 값 추가할려면 튜플을 더해줘야함 숫자 4가 아니라

#딕셔너리 자료형 -> key와 Value가 쌍으로 이루어진 자료형 

a={1:"hi"} # 기본적인 틀
a={'a':[1,2,3]} # Value에 List 추가 가능

a={1:'a'} #Key가 1이고 Value가 'a'
a[2]='b' #Key가 2이고 Value가 'b'인 쌍이 a에 추가됨
a['name']='pey' #Key가 'name'이고 Value가 'pey'인 쌍이 추가
a[3]=[1,2,3] #Key가 3이고 Value가 리스트[1,2,3]인 쌍이 추가
print(a)
del a[1] #Key가 1인 쌍이 삭제됨
print(a)

grade={'pey':10,'julliet':99}
print(grade['pey']) #grade[Key의 요소]를 불러오면 Key에 맞는 Value를 반환함
print(grade['julliet'])
a={1:'a',2:'b'}
print(a[1])
print(a[2])
a={'a':1,'b':2}
print(a['a'])
print(a['b'])

a={1:'a',1:'b'} #key의 값을 같게 한다면 앞의 Value가 무시된다
print(a)

#a={[1,2]:'hi'} -> List를 Key로 사용하면 오류가 뜸. -> 가변인자는 Key로 사용할 수 없음 따라서 튜플은 사용가능.
# 물론 딕셔너리 자신도 Key로 사용할 수 없음, Value는 가변인자 사용 가능

a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys()) #keys()는 딕셔너리의 Key만 모아서 dict_keys객체를 반환함

for k in a.keys(): #for문을 이용해서 key를 반환
    print(k)

print(list(a.keys())) #dict_keys를 리스트로 만들기

print(a.values()) #Value값만 얻기

print(a.items()) #Key와 Value 쌍 모두 값 얻기

a.clear() #a의 Key Value 쌍 모두 지우는 함수
print(a)

a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('name')) #a['name']과 똑같은 기능을 함
print(a.get('phone'))
#print(a['HALO']) #하지만 만약 Key가 딕셔너리 안에 없다면 이것은 오류를 발생시키지만 
#print(a.get('HALO')) #이것은 None을 반환함
print(a.get('foo','bar')) #만약 딕셔너리 안에 Key값이 없을 경우 미리 정해둔 디폴트 값을 대신 반환하게 하는 법

print('name' in a) #딕셔너리 안에 key 값이 있는지 여부 판단하는 함수. 만약 있다면 True를 반환함
print('email' in a) #하지만 없다면 False를 반환함

a={'name':'홍길동','birth':'1128','age':'30'}
print(a.items())

#집합 자료형

s1=set([1,2,3]) #set 자료형 초기화 방법
print(s1)
s2=set("Hello") #이것을 출력하면 {'H', 'l', 'e', 'o'} 이런식으로 나오는데 set는 중복을 허용하지 않고 순서가 없기 때문
print(s2)

s1=set([1,2,3])
l1=list(s1) #set를 리스트로 변환
print(l1)
print(l1[0]) 
t1=tuple(s1) #set를 튜플로 변환
print(t1)
print(t1[0])

#set는 교집합, 차집합, 합집합을 구할때 유용하다.
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1&s2) #교집합 
print(s1.intersection(s2))

print(s1|s2) #합집합
print(s1.union(s2))

print(s1-s2) #차집합
print(s1.difference(s2))

s1=set([1,2,3])
s1.add(4) #set에 값 추가
print(s1)
s1.update([5,6,7]) #여러 값을 추가할려면 update 이용 
print(s1)
s1.remove(6) #set에 값 제거
print(s1)

#bool 자료형 -> True, False를 나타내는 자료형
#자료형에도 참과 거짓이 있음. 특징으로는 문자열, 리스트 튜플, 딕셔너리등 값이 비어있으면 False를 반환하고, 숫자가 0이면 False를 반환함

a=[1,2,3,4] 
while a: #a가 참일동안 -> a가 빈 리스트가 될 때 까지-> 왜냐 [] 이면 False 이기 때문
    print(a.pop())

print(bool([1,2,3])) #리스트에 값이 있으므로 참
print(bool([])) #리스트가 비어있으므로 거짓
print(bool(0)) #0이므로 거짓
print(bool(3)) #0이 아닌 숫자이므로 참

# 자료형의 값을 저장하는 공간, 변수
#C++와 Java와 달리 python은 변수에 저장된 값을 스스로 판단하여 자료형을 지정. 

a=[1,2,3]
print(id(a)) #2251186730688라는 a리스트의 주소값이 반환된다

a=[1,2,3]
b=a #b와 a는 완전히 같은곳을 가르킴(주소가 같다)->동일한 객체
print(a is b) #True가 나온다
a[1]=4 #b도 똑같이 [1,4,3]이 출력된다

#b변수를 가져올 때 a 변수의 값을 가져오면서 다른 주소를 가르키는 방법

#1.
a=[1,2,3]
b=a[:] #a의 첫번째 요소 부터 마지막 까지 슬라이싱을 하기
a[1]=4
print(a)
print(b)

#2.
from copy import copy #copy라는 파이썬 모듈을 이용하기
a=[1,2,3]
b=copy(a)
print(a is b) #False가 나옴. 값은 같지만 내장된 주소가 다르다는 뜻

a,b='python','life' #튜플로 지정
print(a)
print(b)
[a,b]=['python','life'] #리스트로 지정
print(a,b)

a=3
b=5
a,b=b,a #두 변수의 값을 바꿈
print(a,b)

#연습문제

#1.
a=80
b=75
c=55
print("%d" % int((a+b+c)/3))

#2. %로 나머지를 구한 후 0이면 짝수, 1이면 홀수

#3. 
pin="881120-1068234"
yyyymmdd=pin[:6]
num=pin[7:]
print(yyyymmdd)
print(num)

#4.
pin="881120-1068234"
print(pin[7])

#5.
a='a:b:c:d'
b=a.replace(':','#')
print(b)

#6.
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7. 리스트를 공백으로 합치려면 join함수 사용하자!
a=['Life','is','too','short']
result=" ".join(a)
print(result)

#8.
a=(1,2,3)
a=a+(4,) #값을 더하는게 아닌 튜플을 더해야함 -> 튜플을 새로 만드는거라 주소가 바뀜
print(a)

#9. 나머지는 Key가 바뀌지 않는데 [1]는 리스트므로 Key로 사용하기 부적합함

#10.
a={'A':90,'B':80,'C':70}
result = a.pop('B')
print(a)
print(result)

#Q11.
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

#Q12. 똑같은 리스트를 가르키고 있기 때문에 결과가 바뀌어서 출력됨.
'''


























