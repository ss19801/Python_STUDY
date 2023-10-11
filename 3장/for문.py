'''

test_list=['one','two','three']
for i in test_list: #one two three 를 차례로 i에 대입
    print(i)

a=[(1,2),(3,4),(5,6)]
for (first,last) in a: #튜플을 이용한 for문
    print(first+last)    
    
marks = [90,25,67,45,80]
number=0
for mark in marks: 
    number+=1 
    if mark>=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다."%number)
 
        
marks = [90,25,67,45,80]
number=0
for mark in marks:
    number+=1
    if mark<60: continue #continue 문을 이용해 조건에 맞지 않는 점수는 다시 조건문으로 돌아가게 함
    print("%d번 학생 축하합니다. 합격입니다. "%number)

add=0
for i in range (1,11): #1부터 10까지 그 값을 더하라
    add+=i #add에 합산됨
print(add)    

marks=[90,25,67,45,80]
number=0
for number in range(len(marks)): #len을 이용해서 marks의 요소개수를 반환함
    if marks[number]<60: continue
    print("%d번 학생 축하합니다. 합격입니다. "%(number+1))

for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=' ') #구구단 만들기, end=' '를 이용하여 다음줄로 결과값을 넘기지 않게 함
    print('')

a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)

a=[1,2,3,4]
result=[num*3 for num in a if num%2==0] #리스트 내포를 이용, (표현식 for 항복 in 반복가능객체 if 조건) 이 기본적인 틀임 
print(result)

'''


