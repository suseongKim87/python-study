#try, except만 사용하는 경우.
try:
    4/0
except:
    print("error")

#발생 오류를 포함한 try except문. 오류가 일치할 경우 출력.
try:
    4/0
except ZeroDivisionError:
    print("error")

#발생 오류와 메시지 변수를 포함한 try except문
try:
    4/0
except ZeroDivisionError as e:
    print(e)

# try except와 else문
# except에 걸리지 않은 값들은 else문을 통해 추출
try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data=f.read()
    f.close()

# try .. finally 문
# 보통 finally는 사용한 리소스를 close 할 경우에 사용
# f = open('foo.txt', 'w')
# try:
#     print("실행")
# finally:
#     f.close()

# raise로 강제 오류 발생시키기
class Brid:
    def fly(self):
        raise NotImplementedError

# Brid를 상속 받고, fly함수를 정의하지 않았기 때문에 Brid에 있는 fly함수를 받아 error를 발생시킴.
class Eagle(Brid):
    pass

eagle = Eagle()
eagle.fly()

# 아래는 fly함수를 정의한 경우. very fast라는 문구를 출력한다.
class Eagle(Brid):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()