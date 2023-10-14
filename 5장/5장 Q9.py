import sys

numbers=sys.argv[1:]
result=0
for number in numbers:
    result+=number
print(result)