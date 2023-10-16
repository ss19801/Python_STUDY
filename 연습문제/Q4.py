A=[20,55,67,82,45,33,90,87,100,25]
result=0
for i in range(0,10):
    if A[i] >=50:
        result+=A[i]

print(result)

# 답안
result=0
while A:
    mark=A.pop()
    if mark>=50:
        result+=mark
print(result)
