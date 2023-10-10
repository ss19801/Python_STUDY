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

'''





