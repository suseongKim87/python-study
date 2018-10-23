#filter를 사용하지 않는 경우
def positive1(numbers) :
    result = []
    for num in numbers :
        if num > 0:
            result.append(num)

    return result

print(positive1([1,-2,3,-4,5,-6]))

#filter를 사용하는 경우
def positive2(x):
    return x > 0

print(list(filter(positive2, [1,-2,3,-4,5,-6,4])))