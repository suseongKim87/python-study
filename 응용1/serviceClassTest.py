class Service:
    secret = "영구는 배꼽이 두 개다."

    def setname(self, name):
        self.name = name

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a+b
        print("%s님 %s + %s = %s 입니다." %(self.name, a, b, result))

pey = Service("홍길동")
# pey.setname("홍길동")
pey.sum(1,2)

#사칙연산 클래스 만들기
class FourCal:
    def setdata(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b


a=FourCal()
a.setdata(4,2)
print(a.a,"+",a.b,"=",a.sum())
print(a.a,"*",a.b,"=",a.mul())
print(a.a,"-",a.b,"=",a.sub())
print(a.a,"/",a.b,"=",a.div())

b=FourCal()
b.setdata(3,7)
print(b.a,"+",b.b,"=",b.sum())
print(b.a,"*",b.b,"=",b.mul())
print(b.a,"-",b.b,"=",b.sub())
print(b.a,"/",b.b,"=",b.div())

#클래스 기능 만들기
class HousePark:
    lastname = "박"

    def __init__ (self, fullname):
        self.fullname = self.lastname + fullname

    def traval(self, traval):
        self.traval = traval
        return ("%s, %s여행을 가다." % (self.fullname, self.traval))

    def love(self, other):
        print("%s와 %s가 사랑에 빠졌네" % (self.fullname, other.fullname))

    #연산자 오버라이딩
    def __add__(self, other):
        print("%s와 %s가 결혼을 했네" %(self.fullname, other.fullname))

pey = HousePark("응용")
print(pey.traval("부산"))

#클래스상속(inheritance)
class HouseKim(HousePark):
    lastname = "김"

juliet = HouseKim("줄리엣")
print(juliet.traval("독도"))

#클래스 오버라이딩
class HouseLee(HousePark):
    lastname = "이"

    def traval(self, traval, day):
        self.traval = traval
        self.day = day
        return ("%s, %s여행을 %d일 가다." % (self.fullname, self.traval, self.day))

romeo = HouseLee("로미오")
print(romeo.traval("독도",3))

#연산자 오버라이딩
juliet = HouseKim("줄리엣")
romeo = HouseLee("로미오")
juliet+romeo

