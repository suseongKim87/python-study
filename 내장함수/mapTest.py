def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)

    return result

print(two_times([1,2,3,4,5]))

def two_times(x): return x*2

#2.7과 다르게 map을 객체로 판단 하기 때문에 list로 변환해서 출려해야 합니다.
print(map(two_times, [1,2,3,4,5]))
#출력값 : <map object at 0x10df65e80>

print(list(map(two_times, [1,2,3,4,5])))
#[2, 4, 6, 8, 10]
