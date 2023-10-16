f=open('abc.txt','r')
edcba=f.readlines() #저장
f.close()

edcba.reverse()

f=open('abc.txt','w')
for line in edcba:
    line=line.strip() #뒤의 \n문자 지워줌
    f.write(line)
    f.write('\n')
f.close()

