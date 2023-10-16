f=open("sample.txt",'r')
numbers=f.readlines()
f.close()

total=0
for number in numbers:
    num=int(number)
    total+=num
avg=total/len(numbers)

f=open('result.txt','w')
f.write(str(avg))
f.close()