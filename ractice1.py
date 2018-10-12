print("=============  if문 > 다음 코드의 결과값은? =============")
a = "Life is too short you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a:print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
# 답 : shirt
print("===================================================")

print("============= while문 > 별이 증가하는 코드 =============")
i=0
while True:
    i += 1
    if i > 5: break
    print('*'*i)
print("===================================================")

print("============= for문 > 평균점수 구하기 코드 ==============")
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A :
    total += score
average = total/len(A)
print(average)
print("===================================================")