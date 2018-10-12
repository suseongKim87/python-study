marks=[90,25,67,45,80]

print("============= for문 =============")
number=0
for mark in marks:
    number = number+1
    if mark > 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
print("================================")

print("========= continue 사용 =========")
number=0
for mark in marks:
    number = number+1
    if mark < 60:
        continue
    print("%d번 학생은 합격입니다." % number)
print("================================")

print("========== range 사용 ===========")
#rnage(시작숫자, 끝숫자) 끝숫자는 포함하지 않는다.
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생은 합격입니다." % number)
print("================================")

print("========= 구구단 만들기 ===========")
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')
print("================================")
