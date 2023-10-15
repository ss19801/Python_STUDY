import re

p=re.compile('Crow|Servo') # | 문자는 OR 로 사용됨
m=p.match('CrowHello')
print(m)

print(re.search("^Life","Life is too short")) # ^ 문자는 문자열의 맨 처음이 일치하면 매치시켜줌
print(re.search("^Life","My Life")) #이 경우 첫번째 문자열이 아니므로 False

print(re.search('short$',"Life is too short")) # $ 문자는 문자열의 맨 끝이 일치하면 매치
print(re.search('short$','Life is too short, you need python')) #^와 동일

# \A는 문자열의 처음과 매치됨으로 ^와 같은 의미지만 re.MULTILINE에서는 ^는 각줄의 문자열의 처음과 매치되지만 \A는 줄에 상관없이 전체 문자열의 처음과 매치됨
# \Z도 \A와 반대임. 즉 끝과 매치시켜줌

p=re.compile(r'\bclass\b') #\b는 단어 구분자로 보통 whitespace에 의해 구분됨, 꼭 RawString이라는 기호 r을 붙여야함
print(p.search('no class at all'))
print(p.search('one subclass is')) #앞에 sub가 붙어 앞뒤가 whitespace가 아니므로 None 출력 

p=re.compile(r'\Bclass\B') #\b와 반대. whitespace로 구분 된 단어가 아닐경우임.
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))

p=re.compile('(ABC)+') #()를 이용해 그룹을 만듬. 즉 ABC가 반복되면 매치
m=p.search('ABCABCABC OK')
print(m)
print(m.group())

p=re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)") #이런식으로 묶으면 된다
m=p.search("park 010-1234-1234")
print(m.group(1)) #첫번째 그룹 즉 이름이 출력
print(m.group(2)) #두번째 그룹 즉 전화번호가 출력
print(m.group(3)) #세번째 그룹 즉 국번이 출력

p=re.compile(r'(\b\w+)\s+\1') #\1은 재참조 즉 앞의 그룹과 동일한 단어로 매치됨, 두번째 그룹 참조할려면 \2를 씀
print(p.search('Paris is the the sprint').group())

p=re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)') #저 형식으로 그룹에 이름을 붙일수 있음
m=p.search("park 010-1234-1234")
print(m.group('name'))

p=re.compile(r'(?P<word>\b\w+)\s+(?P=word)') #이런식으로 참조 가능.
print(p.search('Paris in the the spring').group())

p=re.compile(".+:")
m=p.search("http://google.com") #http: 가 출력
print(m.group())
p=re.compile(".+(?=:)") #긍정형 전방 탐색을 이용해 :를 생략 가능
m=p.search("http://google.com")
print(m.group())

# .*[.]*.*$ -> 파일이름+.+확장자 를 나타내는 정규식
# 만약 .exe와 .bat를 없애고 싶다면 .*[.](?!bat$|exe$).*$ 를 사용(부정형 전방 탐색)

p=re.compile('(blue|white|red)')
print(p.sub('colour','blue socks and red shoes')) #blue,white,red를 colour로 바꿔줌
print(p.sub('colour','blue socks and red shoes',count=1)) #count를 이용해 첫번째만 바꿔줌
print(p.subn('colour','blue socks and red shoes')) #subn은 튜플로 결과를 반환하는데, 첫번째는 변경된 문자열, 두번째는 요소 바꾸기가 활성화 된 횟수

p=re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p.sub("\g<phone> \g<name>","park 010-1234-1234")) #\g<그룹이름>을 이용하면 참조 가능.

def hexrepl(match):
    value=int(match.group())
    return hex(value)

p=re.compile(r'\d+')
print(p.sub(hexrepl,'Call 65490 for printing, 49152 for user code.')) #매개변수로 함수넣기도 가능

s='<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>',s).span()) #<html> 만 가져오려 해도 *문자는 해당하는 조건에 맞는 문자열을 다 들고옴
print(re.match('<.*>',s).group())
print(re.match('<.*?>',s).group()) #?를 사용하면 *의 탐욕을 막을 수 있음(한번만 출력)

