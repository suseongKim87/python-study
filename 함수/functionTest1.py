# 기본적인 함수를 만드는 방법으로 합을 구하는 합수.
def sum (a,b):
    return a+b

print(sum(1,2))

# 연속되는 값을 받아 처리하는 함수.
def sum_many(*args):
    sum=0

    for i in args :
        sum += i

    return sum

print(sum_many(1,2,3,4,5))

# 여러 입력값을 받은 경우,
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result*i
    return result

print(sum_mul('mul', 1,2,3,4,5,6,7,8,9,10))

#함수의 결과값이 여러개일 경우, 튜플값으로 반환한다.
def sum_and_mul(a, b):
    return a+b, a*b

print(sum_and_mul(1,2))

#위의 튜플값을 2개의 결과 값으로 받고 싶다면 두개의 변수를 적어주면 된다.
sum, mul = sum_and_mul(1,2)
print(sum)
print(mul)

#입력 인수에 초기값 미리 설정하기
def say_myself(name, age, man = True):
    print("name : %s " % name)
    print("age : %d " % age)
    if man:
        print("gender : male")
    else:
        print("gender : female")

say_myself("suseongKim", 32, True)

