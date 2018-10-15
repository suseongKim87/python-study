#파일 생성하기(r:읽기모드, w:쓰기모드, a:추가모드)
#open(파일이름, 열기모드)
f=open("newfile.txt", 'w')
f.close()

#파일을 쓰기모드로 열어 출력값 적기
f=open("newfile2.txt", 'w')
for i in range(1,11):
    data = "%d 번째 줄입니다.\n" %i
    f.write(data)
f.close()

#파일읽기1(readline를 통해 라인별로 읽어 드린다.)
f=open("newfile2.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#파일읽기2(readlines() 함수 이용)
f=open("newfile2.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f=open("newfile2.txt", "r")
data = f.read()
print(data)
f.close()

#파일 추가모드(파일을 읽어 뒤에 데이터를 추가한다.)
f=open("newfile2.txt", "a")
for i in range(11, 21):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

#파일 읽기, 쓰기 모드 with문 (자동으로 file close 할 수 있다.)
with open("test.txt", "w") as f:
    f.write("Life is to short, you need python")

