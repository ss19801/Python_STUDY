#문자 클래스 [] -> []사이의 문자들과 매치 라는 의미를 가짐. [abc],와 [a-c]는 같은 의미를 가짐, 안에 ^을 사용하면 반대라는 의미를 가짐, [^0-9]는 문자가 아닌것 과 매치 라는 뜻
# \d -> [0,9], \D -> [^0-9], \s -> [\t\n\r\f\v]와 같은 의미. whitespace 문자와 매치, \S -> [^\t\n\r\f\v] \s와 반대, \w -> [a-Z0-9_] 문자+숫자와 매치, \W -> [^a-Z0-9] \w와 반대

#Dot(.) -> 줄바꿈 문자인 \n을 제외한 모든 문자와 매치
#a.b -> aab,a0b와는 매치, abc와는 매치가 아님 -> a와 b 사이에 문자가 없기 때문 a[.]b는 a와 b 사이에 .이 와야지 매치됨

# * -> 바로 앞의 문자가 0번부터 무한대 까지 반복 되면 매치
# ca*t -> ct, cat, caat 다 매치

# + -> 최소 1번이상 반복될 때 사용
# ca+t -> cat, caaat는 매치, ct는 매치 X

# {m} -> m번 반복되면 매치
# ca{2}t -> caat면 매치

# {m,n} -> m부터 n번까지 반복되면 매치
# ca{2,5}t -> cat면 매치 X

# ? -> {0,1}을 의미, 있어도 되고 없어도 됨.
# ab?c -> ac, abc면 매치.

'''
import re
p=re.compile('[a-z]+')

m=p.match('python') #match를 이용해 정규식과 매치되는지 조사. 부합하지 않으면 None을 돌려줌, match는 문자열의 처음부터 검색함
if m:
    print('Match found: ', m.group()) #group()를 이용해서 매치되는거 전체 반환
else:
    print('No match')

a=p.search('python')
print(a)
m=p.search("3 python") #search는 match와 달리 문자열 전체를 검색해서 찾음, 따라서 얘도 매치 됨
print(m)

result=p.findall("life is too short") #findall은 단어를 각각 정규식과 매치해서 리스트로 돌려줌
print(result)

result=p.finditer("life is too short") #findall과 동일하지만 반복가능한 객체를 반환함. 객체가 포함하는 요소는 match의 객체임
print(result)
for r in result: print(r) 
'''

'''
import re
p=re.compile('[a-z]+')
m=p.match('python')
print(m.group()) #매치된 문자열 반환
print(m.start()) #매치된 문자열의 시작 위치
print(m.end()) #매치된 문자열의 끝 위치
print(m.span()) #매치된 문자열의 (시작, 끝)에 해당하는 튜플
'''

import re

p=re.compile('a.b') 
m=p.match('a\nb') #원래 . 메타문자는 match를 쓰면 \n문자를 제외한 모든 문자에 매치를 해줌
print(m) #따라서 None이 나옴\
p=re.compile('a.b',re.DOTALL) #하지만 re.DOTALL 옵션을 사용하면 매치 가능, 보통 여러줄로 이루어진 문자에서 \n에 상관없이 검색할 때 사용
m=p.match('a\nb')
print(m)

p=re.compile('[a-z]',re.I) #re.I를 이용하면 대,소문자 구별없이 매치를 수행함
print(p.match("python"))
print(p.match("PYTHON"))

import re
p=re.compile("^python\s\w+") #python 이라는 문자열로 시작하고 뒤에 whitespace, 뒤에 단어가 와야한다는 뜻, ^ 때문에 첫번째만 매치됨
data='''python one
life is too short
python two
you need python
python three
'''
print(p.findall(data))

p=re.compile("^python\s\w+",re.MULTILINE) #multiline을 이용해 one two three 다 출력
print(p.findall(data))

#charref=re.compile(r'&[#](0[0-7]++|[0-9]+|x[0-9a-fA-F]+);')
#charref=re.compile(r"""
#                   &[#]
#                   )0[0-7]+
#                   |[0-9]+
#                   |x[0-9a-fA-F]+)
#                   )
#                   ;
#                  """,re.VERBOSE) #VERBOSE를 이용하면 주석을 이용해 가독성 좋게 사용 가능

p=re.compile('\\\\section') #\\\\를 사용해야지 section을 매치함
p=re.compile(r'\\section') #Raw String 문법을 사용하면 \\ 반복을 막을 수 있음

