def sum(a,b):
    return a + b

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할수 있는 것이 없습니다.")
        return
    else :
        result = sum(a,b)
    return result

"""
$python
>>> import mod1
더할수 있는 것이 없습니다.
None
5
20.4
"""

if __name__=="__main__":
    print(safe_sum('a',1))
    print(safe_sum(1,4))
    print(sum(10, 10.4))

"""
$python
>>> import mod1

#출력값이 존재하지 않음.
"""