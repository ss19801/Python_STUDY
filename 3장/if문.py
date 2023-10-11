'''
#if문

money=True
if money: #money가 True이기 때문에 이 조건문이 실행됨
    print("택시를 타고 가라")
else:
    print("걸어 가라")

money=2000
card=True
if money>=3000 or card: #or, and, not 같은 것들을 이용하여 조건문 만들자
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    
print('a' in ('a','b','c')) #in 을 이용하여 튜플, 리스트, 문자열 안에 조건이 있는지 확인 가능
print('j' in 'python')

pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

pocket=['paper','cellphone','money']
if 'money' in pocket:
    pass #pass를 이용하면 아무값도 반환 하지 않음
else:
    print("걸어 가라")

pocket=['paper','cellphone']
card=True
if 'money' in pocket:
    print("택시를 타고 가라")
elif 'card': #elif를 이용하면 다양한 조건 판별 가능
    print("택시를 타고 가라")
else:
    print("걸어 가라")

if score >= 60:
    message='success'
else:
    message='failure'

message = 'succes' if score >= 60 else 'failure'   #조건부 표현식을 이용해 간단히 작성
    
'''







