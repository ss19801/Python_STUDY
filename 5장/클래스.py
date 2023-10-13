'''
result=0
def add(num):
    global result
    result+=num
    return result

print(add(3))
print(add(4))

class Calculator: #Class로 만든 덧셈 계산
    def __init__(self):
        self.result=0
    
    def add(self,num):
        self.result+=num
        return self.result

cal1=Calculator()
cal2=Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#객체와 인스탄스. 클래스로 만든 객체를 인스턴스라고 하는데, a = Cookie()에서 a는 객체이고 a객체는 Cookie의 인스턴스. 즉 인스턴스는 특정 객체가 어떤 클래스의 객체인지 알려주는 것

class FourCal:
    def __init__(self,first,second): #init을 이용해 생성자 정의
        self.first=first
        self.second=second
        
    def setdata(self,first,second):
        self.first=first
        self.second=second
    
    def add(self):
        result=self.first+self.second
        return result
    
    def sub(self):
        result=self.first-self.second
        return result
    
    def mul(self):
        result=self.first*self.second
        return result

    def div(self):
        result=self.first/self.second
        return result
    
class MoreFourCal(FourCal): #FourCal클래스를 상속하는 MoreFourCal, 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않을 때 상속을 함
    def pow(self):
        result=self.first**self.second
        return result

class SafeFourCal(FourCal): #메서드 오버라이딩을 이용해 div에 조건을 추가함
    def div(self):
        if self.second==0:
            return 0
        else: return self.first/self.second
    
#a=FourCal()
#a.setdata(4,2) #self에는 a가 들어간다.
a=FourCal(4,2) #생성자를 이용해서 a 정의
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
a=MoreFourCal(4,2)
print(a.pow())
a=SafeFourCal(4,0)
print(a.div())

'''



class Family:
    lastname='김' #클래스변수 

a=Family()
b=Family()
print(a.lastname)
print(b.lastname)
print(id(Family.lastname)) #뭘 호출하던 똑같은 id가 나옴, 즉 a,b,Family는 다 같은 메모리를 가지고 있음
print(id(a.lastname))
print(id(b.lastname))
