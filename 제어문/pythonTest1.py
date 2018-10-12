pocket = ['paper','cellphone', 'money']
card = 1

#else if 문을 사용.
if 'money' in pocket:
    print("택시를 타고 가라.")
else:
    if card:
        print("카드를 꺼내라")
    else:
        print("걸어가라")


#else if => elif 로 사용가능.
if 'money' in pocket:
    print("택시를 타고 가라.")
elif card:
    print("택시를 타고 가라.")
else:
    print("걸어가라.")

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    #자바의 String.Format과 비슷한 형태의 구조.
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")


prompt="""
    1.Add
    2.Del
    3.List
    4.Quit

    Enter number:"""

number=0
while number!=4:
    print(prompt)
    number = int(input())