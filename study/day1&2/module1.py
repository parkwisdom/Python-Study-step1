def sum(x, y):
    return x + y

def ssum(x,y):
    print(type(x))
    print(type(y))
    if type(x) != type(y):
        print("데이터 연산 불가")
        return
    else:
        ret = sum(x,y)
        return ret

if __name__=="__main__":#__name__라는 특별한 변수가 있으면 module1이 실행되면 __name__변수의 값으로는 __main__이 저장
    print(ssum('k',5))
    print(ssum(1,5))
    print(ssum(50,3.14))
