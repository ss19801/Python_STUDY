'''
treeHit=0
while treeHit < 10: #While 문 이용, 나무를 10번 찍으면 그만하도록
    treeHit+=1 #treeHit의 개수를 while문 돌때마다 한번씩 올려줌
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit==10:
        print("나무 넘어갑니다.")

        
prompt=""" #여러줄 문자열
1. Add
2. Del
3. List
4. Quit

Enter number: """

number=0
while number != 4: #4를 입력 받을 때 까지 prompt창이 출력됨
    print(prompt)
    number=int(input())

coffee=10
money=300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee-=1
    print("남은 커피의 양은 %d개 입니다."%coffee)
    if coffee==0:
        print("커피가 다 떨어졌습니다.")
        break

a=0
while a<10:
    a+=1
    if a%2==0: continue #continue를 이용해 다시 while문으로 돌아감. 따라서 밑의 print가 실행 되지 않음
    print(a)

while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.") #무한루프를 빠져나갈 때 Ctrl C를 눌러야함    

'''



