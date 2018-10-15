print("==================== 피보나치수열 ====================")
def fib(n):

    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))
print("===================================================")
print("==================== 파일읽고쓰기 =====================")
f=open("sample.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score

average = total/len(lines)

f=open("result.txt", "w")
f.write(str(average))
f.close()
print("===================================================")
