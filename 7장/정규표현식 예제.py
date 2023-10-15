data='''
park 800905-1049118
kim 700905-1059119
'''

result=[]
for line in data.split("\n"): #park 와 kim 나누고
    word_result=[]
    for word in line.split(" "): #공백 사이로 park 와 숫자 나누고
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit(): #만약 숫자라면 
            word=word[:6]+'-'+'*******' #뒷자리를 가림
        word_result.append(word) #word_result에 저장하고
    result.append(' '.join(word_result)) #다시 공백으로 연결시켜줌
print("\n".join(result))

import re

pat=re.compile("(\d{6})[-]\d{7}") #정규표현식을 이용하면 되게 쉽게 변형 가능
print(pat.sub("\g<1>-*******",data))

