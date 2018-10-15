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

class HousePark:
    lastname = "박"

    def __init__ (self, fullname):
        self.fullname = self.lastname + fullname

    def traval(self, traval):
        self.traval = traval
        return ("%s, %s여행을 가다." % (self.fullname, self.traval))

pey = HousePark("응용")
print(pey.traval("부산"))