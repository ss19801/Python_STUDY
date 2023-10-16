input_numbers=input('숫자를 입력하세요: ')
numbers=input_numbers.split(',')
result=0
for i in numbers:
    result+=int(i)
print(result)