a=[1,2,3]
print(id(a))
a=a+[4,5] #+ 연산자 사용시 주소가 바뀜
print(id(a)) 
a=[1,2,3]
print(id(a))
a.extend([4,5]) #extend를 사용 할 경우 주소가 바뀌지 않음
print(id(a))